from apisvc.common.db import etcd as etcd_db


class Manager(object):

    def __init__(self):
        pass

    def get_nodes(self, node_filter):
        node_generator = etcd_db.get_nodes(node_filter=node_filter)

        nodes = []
        for v, k in node_generator:
            nodes.append(k.key)

        return {'result': nodes}

    def get_node(self, node_id, node_roles):
        node = {}

        for role in node_roles:
            v, k = etcd_db.get_node(node_id=node_id, node_role=role)
            node[role] = v

        return {'result': node}

    def get_rings(self, ring_filter):
        ring_generator = etcd_db.get_rings(ring_filter=ring_filter)

        rings = []
        for v, k in ring_generator:
            rings.append(k.key)

        return {'result': rings}

    def create_ring(self, ring_type, account_id, k8s_credential, os_credential):
        # TODO
        return {}