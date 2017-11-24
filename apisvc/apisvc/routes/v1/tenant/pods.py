from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_access
from apisvc.common import check


@ROUTE('/v1/tenant/pods')
@timeit
@check.need_personate_header(check.PERSONATE_TENANT)
@audit_access
def v1_tenant_pods(*args, **kwargs):
    return 'GET /v1/tenant/pods'
