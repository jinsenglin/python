import subprocess
import json
from apisvc.common.log import LOGGER
from apisvc.common import shell


class Manager(object):
    def __init__(self, k8s_credential_path, os_credential_path):
        self._k8s_credential_path = k8s_credential_path
        self._os_credential_path = os_credential_path

    def create_k8s_namespace(self, tenant_id):
        return shell.proxy_kubectl(k8s_credential_path=self._k8s_credential_path,
                                   script_args=['create', 'ns', tenant_id])

    def create_os_project(self, tenant_id):
        return shell.proxy_openstack(os_credential_path=self._os_credential_path,
                                     script_args=['project', 'create', tenant_id])

    def new_k8s_user_cert(self, username, group='system:masters'):
        """
            return a dict object
        """
        return shell.new_k8s_user_cert(username=username, group=group)
