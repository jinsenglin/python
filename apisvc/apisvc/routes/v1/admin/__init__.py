from apisvc import app

@app.route('/v1/admin')
def admin():
    return 'GET /v1/admin'

import tenants
import nodes
