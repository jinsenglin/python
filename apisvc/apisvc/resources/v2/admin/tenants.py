from flask_restful import Resource
from apisvc.common.api import API
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_access
from apisvc.common import check

from apisvc.handlers.v2.admin.tenants import handler_factory
from apisvc.messages.v2.admin.tenants import message_factory


class Tenant(Resource):
    @timeit
    @check.need_personate_header(check.PERSONATE_ADMIN)
    @audit_access
    def get(self, *args, **kwargs):
        # return {'hello': 'world'}
        # return message_factory.new_out_msg_for_get()

        return handler_factory.get(manager=kwargs['apisvc_res_manager'],
                                   in_message=message_factory.new_in_msg_for_get(),
                                   out_message=message_factory.new_out_msg_for_get())

API.add_resource(Tenant, '/v2/admin/tenants')