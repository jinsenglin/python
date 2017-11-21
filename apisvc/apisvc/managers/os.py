import os_client_config
from openstack import connection


class Manager(object):
    def __init__(self, credential=None):
        self._credential = credential

    def demo(self):
        occ = os_client_config.OpenStackConfig(config_files=[self._credential])
        cloud = occ.get_one_cloud('cc-iaas')
        conn = connection.from_config(cloud_config=cloud)
        for server in conn.compute.servers():
            print(server.instance_name)