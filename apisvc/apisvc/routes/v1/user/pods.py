from apisvc import app
from apisvc.common.timeit import timeit

@app.route('/v1/user/pods')
@timeit
def v1_user_pods():
    return 'GET /v1/user/pods'
