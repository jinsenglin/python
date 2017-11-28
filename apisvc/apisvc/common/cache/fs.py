import os
import fasteners
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER


_cache_path = CONFIG['APISVC_CACHE_PATH']


def get_ca_key():
    ca_key = '{0}/ca'.format(_cache_path)
    if os.path.isdir(ca_key):
        LOGGER.debug('ca found')
        return ca_key
    else:
        LOGGER.debug('ca not found')
        return None


def get_ca_pem_keys():
    ca_crt_pem_key = '{0}/ca/crt'.format(_cache_path)
    ca_key_pem_key = '{0}/ca/key'.format(_cache_path)
    return ca_crt_pem_key, ca_key_pem_key


@fasteners.interprocess_locked(CONFIG['APISVC_CACHE_LOCK'])
def put_ca_pems(ca_crt_pem, ca_key_pem):
    ca_key = get_ca_key()

    if ca_key is None:
        ca_key = '{0}/ca'.format(_cache_path)
        os.makedirs(ca_key)
        LOGGER.debug('ca saved'.format())

    ca_crt_pem_key, ca_key_pem_key = get_ca_pem_keys()

    with open(ca_crt_pem_key, 'w') as file_crt:
        file_crt.write(ca_crt_pem)
        LOGGER.debug('pem {0} saved'.format(ca_crt_pem_key))

    with open(ca_key_pem_key, 'w') as file_key:
        file_key.write(ca_key_pem)
        LOGGER.debug('pem {0} saved'.format(ca_key_pem_key))


def get_account_key(account):
    account_key = '{0}/accounts/{1}'.format(_cache_path, account)
    if os.path.isdir(account_key):
        LOGGER.debug('account {0} found'.format(account))
        return account_key
    else:
        LOGGER.debug('account {0} not found'.format(account))
        return None


def get_credential_keys(account):
    credential_key_k8s = '{0}/accounts/{1}/k8s.yaml'.format(_cache_path, account)
    credential_key_os = '{0}/accounts/{1}/os.yaml'.format(_cache_path, account)
    return credential_key_k8s, credential_key_os


@fasteners.interprocess_locked(CONFIG['APISVC_CACHE_LOCK'])
def put_account_and_credentials(account, credential_k8s, credential_os):
    """
    from apisvc.common import util
    util.simulate_time_consuming_op()
    """

    account_key = get_account_key(account)

    if account_key is None:
        account_key = '{0}/accounts/{1}'.format(_cache_path, account)
        os.makedirs(account_key)
        LOGGER.debug('account {0} saved'.format(account))

    credential_key_k8s, credential_key_os = get_credential_keys(account)

    with open(credential_key_k8s, 'w') as file_k8s:
        file_k8s.write(credential_k8s)
        LOGGER.debug('credential {0} saved'.format(credential_key_k8s))

    with open(credential_key_os, 'w') as file_os:
        file_os.write(credential_os)
        LOGGER.debug('credential {0} saved'.format(credential_key_os))
