from apisvc import app

@app.route('/v1/admin/healthz')
def v1_admin_healthz():
    return 'ok'

import tenants
import users
import nodes
