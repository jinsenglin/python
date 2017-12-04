from flask_restful import Resource
from apisvc.common.resource import RESOURCE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_access
from apisvc.common import check
from apisvc.handlers.v2.admin.pools.pool import new_handler
from apisvc.messages.v2.admin.pools.pool import new_message


class Pool(Resource):
    @timeit
    @check.need_personate_header(check.PERSONATE_ADMIN)
    @check.check_body_against_in_message(new_message().input_for_get)
    @audit_access
    def get(self, pool_id, *args, **kwargs):
        return new_handler().get(manager=kwargs['apisvc_res_manager'],
                                 in_message=kwargs['apisvc_in_message'],
                                 out_message=new_message().output_for_get,
                                 pool_id=pool_id)


    @timeit
    @check.need_personate_header(check.PERSONATE_ADMIN)
    @check.check_body_against_in_message(new_message().input_for_put)
    @audit_access
    def put(self, pool_id, *args, **kwargs):
        return new_handler().put(manager=kwargs['apisvc_res_manager'],
                                 in_message=kwargs['apisvc_in_message'],
                                 out_message=new_message().output_for_put,
                                 node_id=pool_id)

    @timeit
    @check.need_personate_header(check.PERSONATE_ADMIN)
    @check.check_body_against_in_message(new_message().input_for_delete)
    @audit_access
    def delete(self, pool_id, *args, **kwargs):
        return new_handler().delete(manager=kwargs['apisvc_res_manager'],
                                    in_message=kwargs['apisvc_in_message'],
                                    out_message=new_message().output_for_delete,
                                    pool_id=pool_id)


RESOURCE.add_resource(Pool, '/v2/admin/pools/<pool_id>')
