from apisvc import app

@app.route('/v1/user/pods')
def pods():
    return 'GET /v1/user/pods'
