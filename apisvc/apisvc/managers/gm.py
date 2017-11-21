from apisvc.managers import k8s
from apisvc.managers import os

class Manager(object):
    # TODO
    def __init__(self, role=None, account=None):
        self._role = role
        self._account = account
        self._k8s_mgr = k8s.Manager()
        self._os_mgr = os.Manager()

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account);
