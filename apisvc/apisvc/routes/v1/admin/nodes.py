from apisvc import app

@app.route('/v1/admin/nodes')
def v1_admin_nodes():
    return 'GET /v1/admin/nodes'
