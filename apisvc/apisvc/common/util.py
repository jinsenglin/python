from apisvc.common.config import CONFIG


def personation_to_role_account(personation):
    return tuple(personation.split(' '))


def account_to_credential_cache(account):
    credential_k8s = '{0}.k8s.yaml'.format(account)
    credential_os = '{0}.os.yaml'.format(account)

    cache = CONFIG['APISVC_CACHE_PATH']
    credential_k8s_cache = '{0}/{1}'.format(cache, credential_k8s)
    credential_os_cache = '{0}/{1}'.format(cache, credential_os)

    return credential_k8s_cache, credential_os_cache
