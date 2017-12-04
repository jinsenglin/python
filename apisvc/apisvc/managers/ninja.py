import subprocess
import json
from apisvc.common.log import LOGGER
from apisvc.common import shell


class Manager(object):
    def __init__(self, k8s_credential_path, os_credential_path):
        self._k8s_credential_path = k8s_credential_path
        self._os_credential_path = os_credential_path

    def new_k8s_user_cert(self, username, group='system:masters'):
        """
            return a dict object
        """
        return shell.new_k8s_user_cert(username=username, group=group)
