from apisvc import app

@app.route('/v1/tenant/healthz')
def v1_tenant_healthz():
    return 'ok'

@app.route('/v1/tenant/quota')
def v1_tenant_quota():
    return 'GET /v1/tenant/quota'

import vms
import pods
