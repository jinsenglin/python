from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "/"

@app.route("/sleep")
def sleep():
    import time
    time.sleep(10)
    return "/sleep"

@app.route("/etcd/put")
def etcd_put():
    import etcd3
    etcd = etcd3.client(host='127.0.0.1')
    etcd.put('/foo', 'bar')
    return "/etcd/put"

@app.route("/etcd/get")
def etcd_get():
    import etcd3
    etcd = etcd3.client(host='127.0.0.1')
    etcd.get('/foo')
    return "/etcd/get"

@app.route("/os/cli")
def os_cli():
    return "TODO"

@app.route("/k8s/cli")
def k8s_cli():
    return "TODO"

@app.route("/os/sdk")
def os_sdk():
    from keystoneauth1 import session as ks_session
    from osc_lib.api import auth
    import openstackclient
    from openstackclient.common import client_config as cloud_config
    from openstackclient.common import clientmanager
    from openstackclient.common import commandmanager
    return "TODO"

@app.route("/k8s/sdk")
def k8s_sdk():
    # TODO check thread-safe
    from kubernetes import client, config
    config.load_kube_config(config_file='../samples/0000-0000-0000-0000.yaml')
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    return "/k8s/sdk"

if __name__ == "__main__":
    app.run()
