from apisvc.common.db import etcd as DB


class Manager(object):

    def __init__(self):
        pass

    def get_nodes(self, node_filter):
        node_generator = DB.get_nodes(node_filter=node_filter)

        nodes = []
        for v, k in node_generator:
            nodes.append(k.key)

        return {'result': nodes}

    def get_node(self, node_id, node_roles):
        node = {}

        for role in node_roles:
            v, k = DB.get_node(node_id=node_id, node_role=role)
            node[role] = v

        return {'result': node}

    def get_rings(self, ring_filter):
        ring_generator = DB.get_rings(ring_filter=ring_filter)

        rings = []
        for v, k in ring_generator:
            rings.append(k.key)

        return {'result': rings}

    def create_ring(self, ring_type, account_id, k8s_credential, os_credential):
        DB.put_ring_and_credentials(role=ring_type,
                                    account=account_id,
                                    credential_k8s=k8s_credential,
                                    credential_os=os_credential)
        return {'result': 'ok'}

    def delete_ring(self, ring_type, account_id):
        DB.del_ring_and_credentials(role=ring_type,
                                    account=account_id)
        return {'result': 'ok'}

    def get_controller(self, target):
        controller, _ = DB.get_controller(target=target)
        return {'result': controller}
