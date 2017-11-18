from apisvc import app
from apisvc.common.profile import timeit

@app.route('/v1/admin/users')
@timeit
def v1_admin_users():
    return 'GET /v1/admin/users'
