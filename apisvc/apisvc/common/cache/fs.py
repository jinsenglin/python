from apisvc.common.config import CONFIG


_cache_path = CONFIG['APISVC_CACHE_PATH']


def get_credential(account):
    credential_k8s = '{0}.k8s.yaml'.format(account)
    credential_k8s_cache = '{0}/{1}'.format(_cache_path, credential_k8s)

    credential_os = '{0}.os.yaml'.format(account)
    credential_os_cache = '{0}/{1}'.format(_cache_path, credential_os)

    return credential_k8s_cache, credential_os_cache
