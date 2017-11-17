from apisvc import app

@app.route('/v1/admin/tenants')
def v1_admin_tenants():
    return 'GET /v1/admin/tenants'
