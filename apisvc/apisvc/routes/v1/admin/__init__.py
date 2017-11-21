from apisvc import app
from apisvc.common.profile import timeit
import tenants
import users
import nodes


@app.route('/v1/admin/healthz')
@timeit
def v1_admin_healthz():
    return 'ok'