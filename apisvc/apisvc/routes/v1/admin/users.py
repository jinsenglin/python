from apisvc import app

@app.route('/v1/admin/users')
def users():
    return 'GET /v1/admin/users'
