class Pools(object):
    def get(self, manager, in_message, out_message, *args, **kwargs):
        # TODO check in_message
        # TODO use manager
        # TODO update out_message
        return out_message, {'Content-Type': 'application/json'}

    def post(self, manager, in_message, out_message, *args, **kwargs):
        # TODO check in_message
        # TODO use manager

        # manager.create_namespace()

        # TODO update out_message
        return out_message, {'Content-Type': 'application/json'}

    def put(self, manager, in_message, out_message, *args, **kwargs):
        # TODO check in_message
        # TODO use manager
        # TODO update out_message
        return out_message, {'Content-Type': 'application/json'}

    def delete(self, manager, in_message, out_message, *args, **kwargs):
        # TODO check in_message
        # TODO use manager
        # TODO update out_message
        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Pools()
