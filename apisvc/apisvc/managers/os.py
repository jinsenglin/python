import os_client_config
from openstack import connection


class Manager(object):
    def __init__(self, credential_path):
        self._credential_path = credential_path

    def create_project(self, tenant_id):
        pass

    def create_user(self, tenant_id, account_id):
        pass
