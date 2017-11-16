from apisvc import app

@app.route('/v1/admin/nodes')
def nodes():
    return 'GET /v1/admin/nodes'
