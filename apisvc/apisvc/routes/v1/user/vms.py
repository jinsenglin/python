from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_access
from apisvc.common import check


@ROUTE('/v1/user/vms')
@timeit
@check.need_personate_header(check.PERSONATE_USER)
@audit_access
def v1_user_vms(*args, **kwargs):
    return 'GET /v1/user/vms'
