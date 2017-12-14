import subprocess
import json
import os
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER
from apisvc.common import util
from apisvc.common.cache import fs as CACHE


_shell_path = CONFIG['APISVC_SHELL_PATH']
_tmp_path = CONFIG['APISVC_TMP_PATH_PROC_WIDE']
_log_path = CONFIG['APISVC_LOG_PATH']


def bash(script_name, script_args=[]):
    LOGGER.debug('script_name = {0}'.format(script_name))

    stdout = None

    script_path = '{0}/{1}'.format(_shell_path, script_name)
    if os.path.isfile(script_path):

        ptt_log_name = '{0}.log'.format(util.get_ptt_string())
        ptt_log_path = '{0}/{1}'.format(_tmp_path, ptt_log_name)
        subprocess_args = ['bash', script_path, _tmp_path] + script_args

        keep_ptt_log = True
        with open(ptt_log_path, 'w') as ptt_log:
            try:
                stdout = subprocess.check_output(subprocess_args, shell=False, stderr=ptt_log)

                # clean up ptt log if exit code is zero
                keep_ptt_log = False

            except subprocess.CalledProcessError:
                LOGGER.critical('failed to run script due to exit code is non-zero')

        if keep_ptt_log:
            os.rename(ptt_log_path, '{0}/{1}'.format(_log_path, ptt_log_name))
            LOGGER.critical('check ptt log {0}/{1} to see more error message'.format(_log_path, ptt_log_name))
        else:
            os.remove(ptt_log_path)

    else:
        LOGGER.error('failed to run script due to script file {0} not found'.format(script_path))

    return stdout


def run_os_script(os_credential_path, script_name, script_args=[], output_format=['-f', 'json']):
    data = None

    auth_url, username, password, project_name, project_domain_name, user_domain_name = util.parse_os_credential_v3(os_credential_path)

    if all(v is not None for v in (auth_url, username, password, project_name, project_domain_name, user_domain_name)):

        extended_script_args = [auth_url, username, password, project_name, project_domain_name, user_domain_name] + script_args + output_format
        stdout = bash(script_name=script_name, script_args=extended_script_args)

        if stdout is not None:
            if len(output_format) > 1 and output_format[1] == 'json':
                try:
                    data = json.loads(stdout)
                except ValueError:
                    LOGGER.critical('failed to run os script due to returned data of invalid json format')
            else:
                data = stdout

    else:
        LOGGER.error('failed to run os script due to invalid credential present')

    return data


def run_k8s_script(k8s_credential_path, script_name, script_args=[], output_format=['-o', 'json']):
    data = None

    extended_script_args = [k8s_credential_path] + script_args + output_format
    stdout = bash(script_name=script_name, script_args=extended_script_args)

    if stdout is not None:
        if len(output_format) > 1 and output_format[1] == 'json':
            try:
                data = json.loads(stdout)
            except ValueError:
                LOGGER.critical('failed to run k8s script due to invalid json format')
        else:
            data = stdout

    return data


def ls_all_k8s_namespaces(k8s_credential_path):
    return run_k8s_script(k8s_credential_path=k8s_credential_path, script_name='ls-all-k8s-namespaces.sh')


def ls_all_os_projects(os_credential_path):
    return run_os_script(os_credential_path=os_credential_path, script_name='ls-all-os-projects.sh')


def proxy_kubectl(k8s_credential_path, script_args=[], output_format=['-o', 'json']):
    return run_k8s_script(k8s_credential_path=k8s_credential_path,
                          script_name='proxy-kubectl.sh',
                          script_args=script_args,
                          output_format=output_format)


def proxy_openstack(os_credential_path, script_args=[], output_format=['-f', 'json']):
    return run_os_script(os_credential_path=os_credential_path,
                         script_name='proxy-openstack.sh',
                         script_args=script_args,
                         output_format=output_format)


def new_k8s_user_cert(ca_crt_path, ca_key_path, username, group='system:masters'):
    """
        return None if ca not found
        return None if subprocess exit code is non-zero
        return a dict object if subprocess exit code is zero
    """

    data = None

    script_args = [ca_crt_path, ca_key_path, username, group]
    stdout = bash(script_name='mk-k8s-user-client-certificate-data.sh', script_args=script_args)

    if stdout is not None:
        try:
            data = json.loads(stdout)
        except ValueError:
            LOGGER.critical('failed to run mk-k8s-user-client-certificate-data.sh script due to returned data of invalid json format')

    return data
