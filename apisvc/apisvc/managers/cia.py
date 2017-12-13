import requests
from apisvc.common.log import LOGGER


class Manager(object):

    def __init__(self):
        pass

    def switch_compute_node_from_os_to_k8s(self, node):
        LOGGER.debug('node = {0}'.format(node))

        endpoint = node['mgmt_endpoint']
        api = '{0}{1}'.format(endpoint, '/v1/role/k8s')
        LOGGER.debug('api = {0}'.format(api))

        result = requests.put(api)
        LOGGER.debug('api result = {0}'.format(result.json()))

        return {'result': result.json()}

    def switch_compute_node_from_k8s_to_os(self, node):
        LOGGER.debug('node = {0}'.format(node))

        endpoint = node['mgmt_endpoint']
        api = '{0}{1}'.format(endpoint, '/v1/role/os')
        LOGGER.debug('api = {0}'.format(api))

        result = requests.put(api)
        LOGGER.debug('api result = {0}'.format(result.json()))

        return {'result': result.json()}