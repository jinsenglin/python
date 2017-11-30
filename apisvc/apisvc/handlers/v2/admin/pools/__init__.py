class Pools(object):

    def get(self, manager, in_message, out_message, *args, **kwargs):
        # TODO
        return out_message, {'Content-Type': 'application/json'}

    def post(self, manager, in_message, out_message, *args, **kwargs):

        # process in_message
        tenant_id = in_message['tenant_id']

        # delegate to manager
        result = manager.create_pool(tenant_id=tenant_id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Pools()
