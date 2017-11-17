from apisvc import app

@app.route('/v1/user/pods')
def v1_user_pods():
    return 'GET /v1/user/pods'
