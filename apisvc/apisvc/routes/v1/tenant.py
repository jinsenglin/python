from apisvc import app

@app.route('/v1/tenant')
def tenant():
    return 'GET /v1/tenant'
