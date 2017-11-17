from apisvc import app

@app.route('/v1/admin/tenants')
def tenants():
    return 'GET /v1/admin/tenants'
