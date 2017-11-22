from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common import check


@ROUTE('/v1/tenant/pods')
@timeit
@check.need_personate_header(check.PERSONATE_TENANT)
def v1_tenant_pods(*args, **kwargs):
    return 'GET /v1/tenant/pods'
