from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "GET /"

@app.route("/bad-request")
def bad_request():
    from flask import abort
    abort(404)
    return "GET /bad-request"

@app.route("/", methods=["POST"])
def post_root():
    return "POST /"

@app.route("/header")
def header():
    from flask import request
    print(request.headers.get('X-PERSONATE'))
    return "GET /header"

@app.route("/json/body", methods=["POST"])
def json_body():
    """Usage: curl -H "Content-Type: application/json" -d '{}' /json/body
    """
    from flask import request
    print(request.get_json())
    return "POST /json/body"

@app.route("/json/return")
def json_return():
    import json
    obj = {}
    obj["status"] = 200
    return json.dumps(obj)

from flask_restful import Resource, Api
class TodoSimple(Resource):
    def get(self, id):
        print(id)
        return "GET /resource"

    def put(self, id):
        print(id)
        return "PUT /resource"

    def delete(self, id):
        print(id)
        return "DELETE /resource"

api = Api(app)
api.add_resource(TodoSimple, '/resource/<string:id>')

@app.route('/res/<string:id>')
def show_post(id):
    print(id)
    return "GET /res"

@app.route("/sleep")
def sleep():
    import time
    time.sleep(10)
    return "GET /sleep"

@app.route("/etcd/put")
def etcd_put():
    import etcd3
    etcd = etcd3.client(host='127.0.0.1')
    etcd.put('/foo', 'bar')
    return "GET /etcd/put"

@app.route("/etcd/get")
def etcd_get():
    import etcd3
    etcd = etcd3.client(host='127.0.0.1')
    etcd.get('/foo')
    return "GET /etcd/get"

@app.route("/os/cli")
def os_cli():
    return "TODO"

@app.route("/k8s/cli")
def k8s_cli():
    return "TODO"

@app.route("/os/sdk")
def os_sdk():
    # TODO utility to generate yaml file from openrc file
    import os_client_config
    occ = os_client_config.OpenStackConfig(config_files=['../samples/0000-0000-0000-0000.os.yaml'])
    cloud = occ.get_one_cloud('cc-iaas')
    from openstack import connection
    conn = connection.from_config(cloud_config=cloud)
    for server in conn.compute.servers():
        print(server.instance_name)
    return "GET /os/sdk"

@app.route("/k8s/sdk")
def k8s_sdk():
    from kubernetes import client, config
    config.load_kube_config(config_file='../samples/0000-0000-0000-0000.k8s.yaml')
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    return "GET /k8s/sdk"

if __name__ == "__main__":
    app.run()
