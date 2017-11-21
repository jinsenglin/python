from apisvc import app
from apisvc.common.profile import timeit
from apisvc.common import check


@app.route('/v1/tenant/pods')
@timeit
@check.need_personate_header(check.PERSONATE_TENANT)
def v1_tenant_pods(*args, **kwargs):
    return 'GET /v1/tenant/pods'