import etcd3
from apisvc.common.config import CONFIG


_host = host = CONFIG['APISVC_DB_HOST']
_client = etcd3.client(host=_host)


# ===================================== #
#                                       #
# ca management                         #
#                                       #
# ===================================== #

def get_ca():
    value, key = _client.get('/apisvc/ca')
    return value, key


def get_ca_pem(target):
    value, key = _client.get('/apisvc/ca/{0}'.format(target))
    return value, key


# ===================================== #
#                                       #
# node management                       #
#                                       #
# ===================================== #


def get_nodes(node_filter):
    node_generator = None

    if node_filter == 'all':
        node_generator = _client.get_prefix('/apisvc/nodes/')
    else:
        node_generator = _client.get_prefix('/apisvc/nodes/{0}/'.format(node_filter))

    return node_generator


def get_node(node_id, node_role):
    value, key = _client.get('/apisvc/nodes/{0}/{1}'.format(node_role, node_id))
    return value, key


# ===================================== #
#                                       #
# controller management                 #
#                                       #
# ===================================== #


def get_controller(target):
    value, key = _client.get('/apisvc/controllers/{0}'.format(target))
    return value, key


# ===================================== #
#                                       #
# ring management                       #
#                                       #
# ===================================== #


def get_rings(ring_filter):
    ring_generator = None

    if ring_filter == 'all':
        ring_generator = _client.get_prefix('/apisvc/rings/')
    else:
        ring_generator = _client.get_prefix('/apisvc/rings/{0}/'.format(ring_filter))

    return ring_generator


def get_ring(role, account):
    value, key = _client.get('/apisvc/rings/{0}/{1}'.format(role, account))
    return value, key


def get_credential(role, account, target):
    value, key = _client.get('/apisvc/rings/{0}/{1}/{2}'.format(role, account, target))
    return value, key


def put_ring_and_credentials(role, account, credential_k8s, credential_os):
    # TODO use transaction to put account and credentials
    _client.put('/apisvc/rings/{0}/{1}'.format(role, account), 'ok')
    _client.put('/apisvc/rings/{0}/{1}/{2}'.format(role, account, 'k8s'), credential_k8s)
    _client.put('/apisvc/rings/{0}/{1}/{2}'.format(role, account, 'os'), credential_os)
