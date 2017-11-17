from apisvc import app

@app.route('/v1/user/vms')
def v1_user_vms():
    return 'GET /v1/user/vms'
