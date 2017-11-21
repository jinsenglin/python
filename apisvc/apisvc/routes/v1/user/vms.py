from apisvc import app
from apisvc.common.profile import timeit
from apisvc.common import check


@app.route('/v1/user/vms')
@timeit
@check.need_personate_header(check.PERSONATE_USER)
def v1_user_vms(*args, **kwargs):
    return 'GET /v1/user/vms'