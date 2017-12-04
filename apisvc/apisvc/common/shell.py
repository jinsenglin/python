import subprocess
import json
import os
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER
from apisvc.common import util
from apisvc.common.db import etcd as etcd_db
from apisvc.common.cache import fs as fs_cache


_shell_path = CONFIG['APISVC_SHELL_PATH']
_tmp_path = CONFIG['APISVC_TMP_PATH_PROC_WIDE']


def bash(script_name, script_args=[]):
    stdout = None

    script_path = '{0}/{1}'.format(_shell_path, script_name)
    if os.path.isfile(script_path):

        ptt_log_name = '{0}.{1}'.format(util.get_ptt_string(), 'log')
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
                LOGGER.critical('check ptt log {0} to see more error message'.format(ptt_log_path))

        if not keep_ptt_log:
            os.remove(ptt_log_path)

    else:
        LOGGER.error('failed to run script due to script file {0} not found'.format(script_path))

    return stdout


def run_os_script(os_credential_path, script_name, script_args=[]):
    data = None

    auth_url, username, password, project_name, project_domain_name, user_domain_name, identity_api_version = util.parse_os_credential_v3(os_credential_path)

    if all(v is not None for v in (auth_url, username, password, project_name, project_domain_name, user_domain_name, identity_api_version)):

        extended_script_args = [auth_url, username, password, project_name, project_domain_name, user_domain_name, identity_api_version] + script_args
        stdout = bash(script_name=script_name, script_args=extended_script_args)

        if stdout is not None:
            try:
                data = json.loads(stdout)
            except ValueError:
                LOGGER.critical('failed to run os script due to returned data of invalid json format')

    else:
        LOGGER.error('failed to run os script due to invalid credential present')

    return data


def run_k8s_script(k8s_credential_path, script_name, script_args=[]):
    data = None

    extended_script_args = [k8s_credential_path] + script_args
    stdout = bash(script_name=script_name, script_args=extended_script_args)

    if stdout is not None:
        try:
            data = json.loads(stdout)
        except ValueError:
            LOGGER.critical('failed to run k8s script due to invalid json format')

    return data


def ls_all_k8s_namespaces(k8s_credential_path):
    return run_k8s_script(k8s_credential_path=k8s_credential_path, script_name='ls-all-k8s-namespaces.sh')


def ls_all_os_projects(os_credential_path):
    return run_os_script(os_credential_path=os_credential_path, script_name='ls-all-os-projects.sh')


def proxy_kubectl(k8s_credential_path, script_args=[]):
    return run_k8s_script(k8s_credential_path=k8s_credential_path,
                         script_name='proxy-kubectl.sh',
                         script_args=script_args)


def proxy_openstack(os_credential_path, script_args=[]):
    return run_os_script(os_credential_path=os_credential_path,
                         script_name='proxy-openstack.sh',
                         script_args=script_args)


def new_k8s_user_cert(username, group='system:masters'):
    """
        return None if ca not found
        return None if subprocess exit code is non-zero
        return a dict object if subprocess exit code is zero
    """

    ca_key = fs_cache.get_ca_key()

    if ca_key is not None:
        LOGGER.debug('ca found in local cache store'.format())
    else:
        LOGGER.debug('ca not found in local cache store'.format())

        _, key = etcd_db.get_ca()
        if key:
            LOGGER.debug('ca found in remote persistent store'.format())
            ca_pem_crt, _ = etcd_db.get_ca_pem('crt')
            ca_pem_key, _ = etcd_db.get_ca_pem('key')
            fs_cache.put_ca_pems(ca_pem_crt, ca_pem_key)
        else:
            LOGGER.debug('ca not found in remote persistent store'.format())
            LOGGER.error('interrupting new_k8s_user_cert due to ca not found in remote persistent store'.format())
            return None

    ca_crt_pem_key, ca_key_pem_key = fs_cache.get_ca_pem_keys()

    try:
        stdout = subprocess.check_output(['bash',
                                          '{0}/{1}'.format(_shell_path, 'mk-k8s-user-client-certificate-data.sh'),
                                          _tmp_path,
                                          ca_crt_pem_key,
                                          ca_key_pem_key,
                                          username,
                                          group], shell=False)

        data = json.loads(stdout)
        LOGGER.debug('key = {0}'.format(data['key']))
        LOGGER.debug('crt = {0}'.format(data['crt']))
        return data

    except subprocess.CalledProcessError:
        LOGGER.critical('failed to make k8s user client certificate data')
        return None
