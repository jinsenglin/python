from apisvc import app
from apisvc.common.profile import timeit

@app.route('/v1/admin/nodes')
@timeit
def v1_admin_nodes():
    return 'GET /v1/admin/nodes'