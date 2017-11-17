from apisvc import app

@app.route('/v1/admin/users')
def v1_admin_users():
    return 'GET /v1/admin/users'
