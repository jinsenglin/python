from apisvc import app

@app.route('/v1/tenant/healthz')
def healthz():
    return 'ok'

@app.route('/v1/tenant/quota')
def quota():
    return 'GET /v1/tenant/quota'

import vms
import pods
