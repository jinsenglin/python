from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common import check


@ROUTE('/v1/admin/vms')
@timeit
@check.need_personate_header(check.PERSONATE_TENANT)
def v1_admin_vms(*args, **kwargs):
    return 'GET /v1/tenant/vms'
