class Nodes(object):

    def get(self, manager, in_message, out_message, *args, **kwargs):
        # process in_message
        filter = in_message['filter']

        # delegate to manager
        result = manager.get_nodes(node_filter=filter)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Nodes()
