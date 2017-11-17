from apisvc import app

@app.route('/v1/admin/healthz')
def healthz():
    return 'ok'

import tenants
import users
import nodes
