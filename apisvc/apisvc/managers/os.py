import os_client_config
from openstack import connection


class Manager(object):
    def __init__(self, credential_path):
        self._credential_path = credential_path
