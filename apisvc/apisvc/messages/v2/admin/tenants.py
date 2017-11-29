class Tenant(object):

    def new_in_msg_for_get(self):
        return {}

    def new_out_msg_for_get(self):
        return {'status': 200, 'result': []}

    def new_in_msg_for_post(self):
        return {}

    def new_out_msg_for_post(self):
        return {}

    def new_in_msg_for_put(self):
        return {}

    def new_out_msg_for_put(self):
        return {}

    def new_in_msg_for_delete(self):
        return {}

    def new_out_msg_for_delete(self):
        return {}


message_factory = Tenant()
