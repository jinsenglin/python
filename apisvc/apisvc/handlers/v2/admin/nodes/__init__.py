class Nodes(object):

    def get(self, manager, in_message, out_message, *args, **kwargs):
        # TODO
        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Nodes()
