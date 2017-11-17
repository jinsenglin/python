from apisvc import app

@app.route('/v1/admin/vms')
def vms():
    return 'GET /v1/tenant/vms'
