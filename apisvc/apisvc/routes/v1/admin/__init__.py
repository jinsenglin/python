from apisvc import app
from apisvc.common.timeit import timeit

@app.route('/v1/admin/healthz')
@timeit
def v1_admin_healthz():
    return 'ok'

import tenants
import users
import nodes
