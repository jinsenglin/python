from apisvc import app

@app.route('/v1/tenant/pods')
def pods():
    return 'GET /v1/tenant/pods'
