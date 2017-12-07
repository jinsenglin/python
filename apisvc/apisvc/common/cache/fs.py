import os
import fasteners
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER


_cache_path = CONFIG['APISVC_CACHE_PATH']


def _get_ca_key():
    return '{0}/ca'.format(_cache_path)


def _get_ca_pem_keys():
    return '{0}/ca/crt'.format(_cache_path),\
           '{0}/ca/key'.format(_cache_path)


def _get_ring_key(role, account):
    return '{0}/rings/{1}/{2}'.format(_cache_path, role, account)


def _get_credential_keys(role, account):
    return '{0}/rings/{1}/{2}/k8s.yaml'.format(_cache_path, role, account),\
           '{0}/rings/{1}/{2}/os.yaml'.format(_cache_path, role, account)


def get_ca_key():
    ca_key = _get_ca_key()
    if os.path.isdir(ca_key):
        LOGGER.debug('ca found')
        return ca_key
    else:
        LOGGER.debug('ca not found')
        return None


def get_ca_pem_keys():
    ca_crt_pem_key, ca_key_pem_key = _get_ca_pem_keys()
    return ca_crt_pem_key, ca_key_pem_key


@fasteners.interprocess_locked(CONFIG['APISVC_LOCK_FILE'])
def put_ca_pems(ca_crt_pem, ca_key_pem):
    ca_key = get_ca_key()

    if ca_key is None:
        ca_key = _get_ca_key()
        os.makedirs(ca_key)
        LOGGER.debug('ca saved'.format())

    ca_crt_pem_key, ca_key_pem_key = get_ca_pem_keys()

    with open(ca_crt_pem_key, 'w') as file_crt:
        file_crt.write(ca_crt_pem)
        LOGGER.debug('pem {0} saved'.format(ca_crt_pem_key))

    with open(ca_key_pem_key, 'w') as file_key:
        file_key.write(ca_key_pem)
        LOGGER.debug('pem {0} saved'.format(ca_key_pem_key))


def get_ring_key(role, account):
    ring_key = _get_ring_key(role=role, account=account)
    if os.path.isdir(ring_key):
        LOGGER.debug('ring for role {0} account {1} found'.format(role, account))
        return ring_key
    else:
        LOGGER.debug('ring for role {0} account {1} not found'.format(role, account))
        return None


def get_credential_keys(role, account):
    credential_key_k8s, credential_key_os = _get_credential_keys(role=role, account=account)
    return credential_key_k8s, credential_key_os


@fasteners.interprocess_locked(CONFIG['APISVC_LOCK_FILE'])
def put_ring_and_credentials(role, account, credential_k8s, credential_os):
    """
    from apisvc.common import util
    util.simulate_time_consuming_op()
    """

    ring_key = get_ring_key(role=role, account=account)

    if ring_key is None:
        ring_key = _get_ring_key(role=role, account=account)
        os.makedirs(ring_key)
        LOGGER.debug('ring for role {0} account {1} saved'.format(role, account))

    credential_key_k8s, credential_key_os = get_credential_keys(role=role, account=account)

    with open(credential_key_k8s, 'w') as file_k8s:
        file_k8s.write(credential_k8s)
        LOGGER.debug('credential {0} saved'.format(credential_key_k8s))

    with open(credential_key_os, 'w') as file_os:
        file_os.write(credential_os)
        LOGGER.debug('credential {0} saved'.format(credential_key_os))
