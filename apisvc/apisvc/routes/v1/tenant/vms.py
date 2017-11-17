from apisvc import app

@app.route('/v1/admin/vms')
def v1_admin_vms():
    return 'GET /v1/tenant/vms'
