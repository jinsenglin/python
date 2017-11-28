from apisvc.common.cache import fs as fs_cache
from apisvc.managers import k8s
from apisvc.managers import os
from apisvc.managers import cia
from apisvc.managers import la
from apisvc.common.log import LOGGER


class Manager(object):
    def __init__(self, role=None, account=None):
        self._role = role
        self._account = account

        credential_key_k8s, credential_key_os = fs_cache.get_credential_keys(account)
        self._k8s_mgr = k8s.Manager(credential_key=credential_key_k8s)
        self._os_mgr = os.Manager(credential_key=credential_key_os)
        self._cia_mgr = cia.Manager()
        self._la_mgr = la.Manager()

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account)

    def demo(self):
        self._k8s_mgr.demo()
        self._os_mgr.demo()
        self._cia_mgr.demo()
        self._la_mgr.demo()

    def create_namespace(self):
        self._la_mgr.mk_ks8_user_client_certificate_data('cclin')
        LOGGER.debug('create_namespace')

    def create_account(self):
        LOGGER.debug('create_account')
