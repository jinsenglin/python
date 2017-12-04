class Node(object):

    def get(self, manager, in_message, out_message, node_id, *args, **kwargs):
        # delegate to manager
        result = manager.get_node(node_id=node_id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}

    def put(self, manager, in_message, out_message, node_id, *args, **kwargs):
        # delegate to manager
        result = manager.update_node(node_id=node_id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Node()
