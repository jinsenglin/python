import json
from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access


@ROUTE('/proxy', methods=['POST'])
@timeit
@audit_anonymous_access
def proxy():
    from flask import request
    from apisvc.common import shell
    result = shell.proxy_openstack(os_credential_path='samples/0000-0000-0000-0000.os.yaml',
                          script_args=['project', 'list'],
                          output_format=['-f', 'json'])
    # request.get_json()
    return json.dumps({'status': 200, 'data': result}), \
           {'Content-Type': 'application/json'}
