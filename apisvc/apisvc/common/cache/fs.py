import os
from apisvc.common.config import CONFIG


_cache_path = CONFIG['APISVC_CACHE_PATH']


def get_account(account):
    account_cached = '{0}/{1}'.format(_cache_path, account)
    if os.path.isdir(account_cached):
        return account_cached
    else:
        return None


def get_credential(account):
    credential_k8s_cached = '{0}/{1}/k8s.yaml'.format(_cache_path, account)
    credential_os_cached = '{0}/{1}/os.yaml'.format(_cache_path, account)
    return credential_k8s_cached, credential_os_cached
