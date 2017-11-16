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
    return "TODO"

@app.route("/etcd/get")
def etcd_get():
    return "TODO"

@app.route("/os/cli")
def etcd_put():
    return "TODO"

@app.route("/k8s/cli")
def etcd_get():
    return "TODO"

@app.route("/os/sdk")
def etcd_put():
    return "TODO"

@app.route("/k8s/sdk")
def etcd_get():
    return "TODO"

if __name__ == "__main__":
    app.run()
