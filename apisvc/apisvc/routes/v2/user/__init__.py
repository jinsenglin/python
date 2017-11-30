import json
from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access


@ROUTE('/v2/user/healthz')
@timeit
@audit_anonymous_access
def v2_user_healthz():
    return 'ok', {'Content-Type': 'text/plain'}


@ROUTE('/v2/user/apis')
@timeit
@audit_anonymous_access
def v2_user_apis():
    return json.dumps({'status': 200,
                       'data': [{'method': 'GET', 'path': '/v2/user/healthz'},
                                {'method': 'GET', 'path': '/v2/user/apis'}
                                ]}), \
           {'Content-Type': 'application/json'}
