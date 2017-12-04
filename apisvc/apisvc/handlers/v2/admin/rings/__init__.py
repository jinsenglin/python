class Rings(object):

    def get(self, manager, in_message, out_message, *args, **kwargs):
        # process in_message
        ring_filter = in_message['filter']

        # delegate to manager
        result = manager.get_rings(ring_filter=ring_filter)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}

    def post(self, manager, in_message, out_message, *args, **kwargs):
        # process in_message
        tenant_id = in_message['tenant_id']
        account_id = in_message['account_id']

        # delegate to manager
        result = manager.create_ring(tenant_id=tenant_id, account_id=account_id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Rings()
