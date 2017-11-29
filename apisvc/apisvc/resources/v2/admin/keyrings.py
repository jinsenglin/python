from flask_restful import Resource
from apisvc.common.resource import RESOURCE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_access
from apisvc.common import check
from apisvc.handlers.v2.admin.keyrings import new_handler
from apisvc.messages.v2.admin.keyrings import new_message


class Keyring(Resource):
    @timeit
    @check.need_personate_header(check.PERSONATE_ADMIN)
    @check.check_body_against_in_message(new_message().input_for_get)
    @audit_access
    def get(self, *args, **kwargs):
        return new_handler().get(manager=kwargs['apisvc_res_manager'],
                                 in_message=kwargs['apisvc_in_message'],
                                 out_message=new_message().output_for_get)

    @timeit
    @check.need_personate_header(check.PERSONATE_ADMIN)
    @check.check_body_against_in_message(new_message().input_for_post)
    @audit_access
    def post(self, *args, **kwargs):
        return new_handler().post(manager=kwargs['apisvc_res_manager'],
                                  in_message=kwargs['apisvc_in_message'],
                                  out_message=new_message().output_for_post)

    @timeit
    @check.need_personate_header(check.PERSONATE_ADMIN)
    @check.check_body_against_in_message(new_message().input_for_put)
    @audit_access
    def put(self, *args, **kwargs):
        return new_handler().put(manager=kwargs['apisvc_res_manager'],
                                 in_message=kwargs['apisvc_in_message'],
                                 out_message=new_message().output_for_put)

    @timeit
    @check.need_personate_header(check.PERSONATE_ADMIN)
    @check.check_body_against_in_message(new_message().input_for_delete)
    @audit_access
    def delete(self, *args, **kwargs):
        return new_handler().delete(manager=kwargs['apisvc_res_manager'],
                                    in_message=kwargs['apisvc_in_message'],
                                    out_message=new_message().output_for_delete)


RESOURCE.add_resource(Keyring, '/v2/admin/keyrings')
