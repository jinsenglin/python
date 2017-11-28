from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_access
from apisvc.common import check
from apisvc.handlers.v1.admin.tenants import v1_admin_tenants_post as v1_admin_tenants_post_handler
from apisvc.responses.v1.admin.tenants import v1_admin_tenants_post as v1_admin_tenants_post_response
from apisvc.requests.v1.admin.tenants import v1_admin_tenants_post as v1_admin_tenants_post_request


@ROUTE('/v1/admin/tenants')
@timeit
@check.need_personate_header(check.PERSONATE_ADMIN)
@audit_access
def v1_admin_tenants(*args, **kwargs):
    return 'GET /v1/admin/tenants'


@ROUTE('/v1/admin/tenants', methods=['POST'])
@timeit
@check.need_personate_header(check.PERSONATE_ADMIN)
@audit_access
def v1_admin_tenants_post(*args, **kwargs):
    return v1_admin_tenants_post_handler(manager=kwargs['apisvc_res_manager'],
                                         request=v1_admin_tenants_post_request,
                                         response=v1_admin_tenants_post_response)
