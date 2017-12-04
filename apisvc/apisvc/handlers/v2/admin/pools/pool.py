class Pool(object):

    def get(self, manager, in_message, out_message, pool_id, *args, **kwargs):
        # delegate to manager
        result = manager.get_pool(pool_id=pool_id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}

    def put(self, manager, in_message, out_message, pool_id, *args, **kwargs):
        # delegate to manager
        result = manager.update_pool(pool_id=pool_id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}

    def delete(self, manager, in_message, out_message, pool_id, *args, **kwargs):
        # delegate to manager
        result = manager.delete_pool(pool_id=pool_id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Pool()
