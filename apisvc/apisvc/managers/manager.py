from apisvc.managers.k8s import Kubernetes
from apisvc.managers.os import OpenStack

class Manager(object):
    # TODO
    def __init__(self, role=None, account=None):
        self._role = role
        self._account = account
        self._k8s = Kubernetes()
        self._os = OpenStack()

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account);
