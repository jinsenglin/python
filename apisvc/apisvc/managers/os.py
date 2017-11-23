import os_client_config
from openstack import connection


class Manager(object):
    def __init__(self, credential_key=None):
        self._credential_key = credential_key

    def demo(self):
        occ = os_client_config.OpenStackConfig(config_files=[self._credential_key])
        cloud = occ.get_one_cloud('os')
        conn = connection.from_config(cloud_config=cloud)
        for server in conn.compute.servers():
            print(server.instance_name)