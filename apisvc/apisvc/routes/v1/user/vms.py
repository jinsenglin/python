from apisvc import app
from apisvc.common.timeit import timeit

@app.route('/v1/user/vms')
@timeit
def v1_user_vms():
    return 'GET /v1/user/vms'
