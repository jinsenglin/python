import json
from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access


@ROUTE('/mock/comp1/v1/healthz')
@timeit
@audit_anonymous_access
def mock_comp1_v1_healthz():
    return 'comp1 ok', {'Content-Type': 'text/plain'}


@ROUTE('/mock/comp1/v1/role/os', methods=["PUT"])
@timeit
@audit_anonymous_access
def mock_comp1_v1_role_os():
    return json.dumps({'status': 200}), \
           {'Content-Type': 'application/json'}


@ROUTE('/mock/comp1/v1/role/k8s', methods=["PUT"])
@timeit
@audit_anonymous_access
def mock_comp1_v1_role_k8s():
    return json.dumps({'status': 200}), \
           {'Content-Type': 'application/json'}
