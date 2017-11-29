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
    return {'status': 200,
            'message': [{'method': 'GET', 'path': '/healthz'},
                        {'method': 'GET', 'path': '/apis'}]}, {'Content-Type': 'application/json'}
