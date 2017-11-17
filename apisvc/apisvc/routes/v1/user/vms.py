from apisvc import app

@app.route('/v1/user/vms')
def vms():
    return 'GET /v1/user/vms'
