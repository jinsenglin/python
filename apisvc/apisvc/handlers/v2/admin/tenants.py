class Tenant(object):
    def get(self, manager, in_message, out_message, *args, **kwargs):
        return out_message, {'Content-Type': 'application/json'}

handler_factory = Tenant()
