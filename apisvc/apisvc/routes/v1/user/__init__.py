from apisvc import app

@app.route('/v1/user/healthz')
def v1_user_healthz():
    return 'ok'

import vms
import pods
