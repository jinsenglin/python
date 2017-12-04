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
