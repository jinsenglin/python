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
    return "TODO"

@app.route("/k8s/sdk")
def k8s_sdk():
    return "TODO"

if __name__ == "__main__":
    app.run()
