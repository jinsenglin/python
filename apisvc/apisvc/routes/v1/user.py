from apisvc import app

@app.route('/v1/user')
def user():
    return 'GET /v1/user'
