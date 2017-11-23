import os
import fasteners
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER


_cache_path = CONFIG['APISVC_CACHE_PATH']


def get_account_key(account):
    account_key = '{0}/{1}'.format(_cache_path, account)
    if os.path.isdir(account_key):
        LOGGER.debug('account {0} found'.format(account))
        return account_key
    else:
        LOGGER.debug('account {0} not found'.format(account))
        return None


def get_credential_keys(account):
    credential_key_k8s = '{0}/{1}/k8s.yaml'.format(_cache_path, account)
    credential_key_os = '{0}/{1}/os.yaml'.format(_cache_path, account)
    return credential_key_k8s, credential_key_os


@fasteners.interprocess_locked(CONFIG['APISVC_CACHE_LOCK'])
def put_account_and_credentials(account, credential_k8s, credential_os):
    """
    from apisvc.common import util
    util.simulate_time_consuming_op()
    """

    account_key = get_account_key(account)

    if account_key is None:
        account_key = '{0}/{1}'.format(_cache_path, account)
        os.makedirs(account_key)
        LOGGER.debug('account {0} saved'.format(account))

    credential_key_k8s, credential_key_os = get_credential_keys(account)

    with open(credential_key_k8s, 'w') as file_k8s:
        file_k8s.write(credential_k8s)
        LOGGER.debug('credential {0} saved'.format(credential_key_k8s))

    with open(credential_key_os, 'w') as file_os:
        file_os.write(credential_os)
        LOGGER.debug('credential {0} saved'.format(credential_key_os))
