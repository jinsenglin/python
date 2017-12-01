import subprocess
import json
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER
from apisvc.common.db import etcd as etcd_db
from apisvc.common.cache import fs as fs_cache


_shell_path = CONFIG['APISVC_SHELL_PATH']
_tmp_path = CONFIG['APISVC_TMP_PATH']


def ls_all_k8s_namespaces(k8s_credential_path):
    try:
        stdout = subprocess.check_output(['bash',
                                          '{0}/{1}'.format(_shell_path, 'ls-all-k8s-namespaces.sh'),
                                          _tmp_path,
                                          'http://192.168.228.31:5000/v2.0/',
                                          'RegionOne',
                                          'jimlin',
                                          'jimlin',
                                          'jimlin'], shell=False)

        data = json.loads(stdout)
        LOGGER.debug('data = {0}'.format(data))
        return data

    except subprocess.CalledProcessError as e:
        LOGGER.critical('failed to list k8s namespaces')
        return None


def ls_all_os_projects(os_credential_path):
    try:
        stdout = subprocess.check_output(['bash',
                                          '{0}/{1}'.format(_shell_path, 'ls-all-os-projects.sh'),
                                          _tmp_path,
                                          'http://192.168.228.31:5000/v2.0/',
                                          'RegionOne',
                                          'jimlin',
                                          'jimlin',
                                          'jimlin'], shell=False)

        data = json.loads(stdout)
        LOGGER.debug('data = {0}'.format(data))
        return data

    except subprocess.CalledProcessError as e:
        LOGGER.critical('failed to list os projects')
        return None


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

    except subprocess.CalledProcessError as e:
        LOGGER.critical('failed to make k8s user client certificate data')
        return None
