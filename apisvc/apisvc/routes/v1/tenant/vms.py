from apisvc import app
from apisvc.common.profile import timeit

@app.route('/v1/admin/vms')
@timeit
def v1_admin_vms():
    return 'GET /v1/tenant/vms'