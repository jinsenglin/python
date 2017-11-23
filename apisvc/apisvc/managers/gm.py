from apisvc.common.cache import fs as fs_cache
from apisvc.managers import k8s
from apisvc.managers import os
from apisvc.managers import cia


class Manager(object):
    def __init__(self, role=None, account=None):
        self._role = role
        self._account = account

        credential_key_k8s, credential_key_os = fs_cache.get_credential_keys(account)
        self._k8s_mgr = k8s.Manager(credential_key=credential_key_k8s)
        self._os_mgr = os.Manager(credential_key=credential_key_os)
        self._cia_mgr = cia.Manager()

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account)

    def demo(self):
        self._k8s_mgr.demo()
        self._os_mgr.demo()
        self._cia_mgr.demo()
