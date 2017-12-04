class Node(object):

    def get(self, manager, in_message, out_message, node_id, *args, **kwargs):
        # process in_message
        roles = in_message['roles']

        # delegate to manager
        result = manager.get_node(node_id=node_id, node_roles=roles)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}

    def put(self, manager, in_message, out_message, node_id, *args, **kwargs):
        # process in_message
        role = in_message['role']

        # delegate to manager
        result = manager.update_node(node_id=node_id, node_role=role)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Node()
