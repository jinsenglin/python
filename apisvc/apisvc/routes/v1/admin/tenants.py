from apisvc import app
from apisvc.common.profile import timeit

@app.route('/v1/admin/tenants')
@timeit
def v1_admin_tenants():
    return 'GET /v1/admin/tenants'
