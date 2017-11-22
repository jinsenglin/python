from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common import check


@ROUTE('/v1/admin/nodes')
@timeit
@check.need_personate_header(check.PERSONATE_ADMIN)
def v1_admin_nodes(*args, **kwargs):
    return 'GET /v1/admin/nodes'
