from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access


@ROUTE('/v2/admin/healthz')
@timeit
@audit_anonymous_access
def v2_admin_healthz():
    return 'ok', {'Content-Type': 'text/plain'}


@ROUTE('/v2/admin/apis')
@timeit
@audit_anonymous_access
def v2_admin_apis():
    return {'status': 200,
            'message': [{'method': 'GET', 'path': '/healthz'},
                        {'method': 'GET', 'path': '/apis'}]}, {'Content-Type': 'application/json'}
