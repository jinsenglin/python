from apisvc import app
from apisvc.common.profile import timeit

@app.route('/v1/user/healthz')
@timeit
def v1_user_healthz():
    return 'ok'

import vms
import pods
