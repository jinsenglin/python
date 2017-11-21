from apisvc.common import util
from apisvc.managers import k8s
from apisvc.managers import os


class Manager(object):
    def __init__(self, role=None, account=None):
        self._role = role
        self._account = account

        credential_k8s_cache, credential_os_cache=util.credential_cache(account)
        self._k8s_mgr = k8s.Manager(credential=credential_k8s_cache)
        self._os_mgr = os.Manager(credential=credential_os_cache)

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account)

    def demo(self):
        self._k8s_mgr.demo()
        self._os_mgr.demo()
