import os
import fasteners
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER


_cache_path = CONFIG['APISVC_CACHE_PATH']


def get_account(account):
    account_cached = '{0}/{1}'.format(_cache_path, account)
    if os.path.isdir(account_cached):
        LOGGER.debug('account {0} found'.format(account))
        return account_cached
    else:
        LOGGER.debug('account {0} not found'.format(account))
        return None


def get_credential(account):
    credential_k8s_cached = '{0}/{1}/k8s.yaml'.format(_cache_path, account)
    credential_os_cached = '{0}/{1}/os.yaml'.format(_cache_path, account)
    return credential_k8s_cached, credential_os_cached


@fasteners.interprocess_locked(CONFIG['APISVC_CACHE_LOCK'])
def put_account_and_credentials(account, credential_k8s, credential_os):
    """
    LOGGER.debug('..............................lock got')
    import time
    LOGGER.debug('..............................sleeping')
    time.sleep(10)
    LOGGER.debug('...............................wake up')
    """

    account_cached = get_account(account)

    if account_cached is None:
        account_cached = '{0}/{1}'.format(_cache_path, account)
        os.makedirs(account_cached)
        LOGGER.debug('account {0} saved'.format(account))

    credential_k8s_cached, credential_os_cached = get_credential(account)

    with open(credential_k8s_cached, 'w') as file_k8s:
        file_k8s.write(credential_k8s)
        LOGGER.debug('credential {0} saved'.format(credential_k8s_cached))

    with open(credential_os_cached, 'w') as file_os:
        file_os.write(credential_os)
        LOGGER.debug('credential {0} saved'.format(credential_os_cached))
