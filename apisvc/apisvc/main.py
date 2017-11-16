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
    # TODO utility to generate yaml file from openrc file
    # TODO switch cloud
    # TODO check thread-safe
    import os_client_config
    occ = os_client_config.OpenStackConfig()
    cloud = occ.get_one_cloud('cc-iaas')
    from openstack import connection
    conn = connection.from_config(cloud_config=cloud)
    for server in conn.compute.servers():
        print(server.instance_name)
    return "/os/sdk"

@app.route("/k8s/sdk")
def k8s_sdk():
    # TODO check thread-safe
    from kubernetes import client, config
    config.load_kube_config(config_file='../samples/0000-0000-0000-0000.k8s.yaml')
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    return "/k8s/sdk"

if __name__ == "__main__":
    app.run()
