import os_client_config
from openstack import connection


class Manager(object):
    def __init__(self, credential_path):
        self._credential_path = credential_path

        occ = os_client_config.OpenStackConfig(config_files=[self._credential_path])
        self._cloud_config = occ.get_one_cloud('os')

    def create_project(self, tenant_id):
        conn = connection.from_config(cloud_config=self._cloud_config)
        pass

    def create_user(self, tenant_id, account_id):
        pass
