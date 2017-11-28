from flask_restful import Resource
from apisvc.common.api import API


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


API.add_resource(HelloWorld, '/v2/admin/tenants')