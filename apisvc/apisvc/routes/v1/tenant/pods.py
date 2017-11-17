from apisvc import app

@app.route('/v1/tenant/pods')
def v1_tenant_pods():
    return 'GET /v1/tenant/pods'
