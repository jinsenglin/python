from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common import check


@ROUTE('/v1/user/pods')
@timeit
@check.need_personate_header(check.PERSONATE_USER)
def v1_user_pods(*args, **kwargs):
    return 'GET /v1/user/pods'
