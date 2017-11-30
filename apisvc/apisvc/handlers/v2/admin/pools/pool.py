class Pool(object):

    def get(self, manager, in_message, out_message, id, *args, **kwargs):
        # delegate to manager
        result = manager.get_pool(id=id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}

    def put(self, manager, in_message, out_message, id, *args, **kwargs):
        # delegate to manager
        result = manager.update_pool(id=id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}

    def delete(self, manager, in_message, out_message, id, *args, **kwargs):
        # delegate to manager
        result = manager.delete_pool(id=id)

        # TODO may process result

        # update out_message
        out_message.update(result)

        return out_message, {'Content-Type': 'application/json'}


def new_handler():
    return Pool()
