from apisvc.common.log import LOGGER
from apisvc.common import shell


class Manager(object):
    def __init__(self, k8s_credential_path, os_credential_path, ca_crt_path, ca_key_path):
        self._k8s_credential_path = k8s_credential_path
        self._os_credential_path = os_credential_path
        self._ca_crt_path = ca_crt_path
        self._ca_key_path = ca_key_path

    def create_k8s_namespace(self, tenant_id):
        return shell.proxy_kubectl(k8s_credential_path=self._k8s_credential_path,
                                   script_args=['create', 'ns', tenant_id])

    def delete_k8s_namespace(self, tenant_id):
        return shell.proxy_kubectl(k8s_credential_path=self._k8s_credential_path,
                                   script_args=['delete', 'ns', tenant_id],
                                   output_format=['-o', 'name'])

    def create_os_project(self, tenant_id):
        return shell.proxy_openstack(os_credential_path=self._os_credential_path,
                                     script_args=['project', 'create', tenant_id])

    def delete_os_project(self, tenant_id):
        return shell.proxy_openstack(os_credential_path=self._os_credential_path,
                                     script_args=['project', 'delete', tenant_id])

    def create_os_user(self, tenant_id, account_id):
        return shell.proxy_openstack(os_credential_path=self._os_credential_path,
                                     script_args=['user', 'create',
                                                  '--project', tenant_id,
                                                  '--password', 'pass', account_id])

    def create_k8s_user(self, tenant_id, account_id):
        return self.new_k8s_user_cert(username=account_id)

    def new_k8s_user_cert(self, username, group='system:masters'):
        return shell.new_k8s_user_cert(ca_crt_path=self._ca_crt_path,
                                       ca_key_path=self._ca_key_path,
                                       username=username,
                                       group=group)
