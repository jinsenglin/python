from kubernetes import client, config


class Manager(object):

    def __init__(self, credential_path):
        self._credential_path = credential_path

    def create_namespace(self, tenant_id):
        pass
