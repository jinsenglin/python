from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_access
from apisvc.common import check


@ROUTE('/v1/admin/tenants')
@timeit
@check.need_personate_header(check.PERSONATE_ADMIN)
@audit_access
def v1_admin_tenants(*args, **kwargs):
    return 'GET /v1/admin/tenants'
