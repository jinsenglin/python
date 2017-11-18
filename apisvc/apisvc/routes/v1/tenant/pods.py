from apisvc import app
from apisvc.common.profile import timeit

@app.route('/v1/tenant/pods')
@timeit
def v1_tenant_pods():
    return 'GET /v1/tenant/pods'
