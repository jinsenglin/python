from apisvc import app

@app.route('/v1/user/healthz')
def healthz():
    return 'ok'

import vms
import pods
