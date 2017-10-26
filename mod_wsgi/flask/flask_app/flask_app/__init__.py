from flask import Flask
app = Flask(__name__)


@app.route("/")
def root():
    return "Root"


@app.route("/hello")
def hello():
    return "Hello"


@app.route("/auth/always_deny", methods=["GET", "POST"])
def auth_always_deny():
    import json
    obj = {}
    obj["apiVersion"] = "authentication.k8s.io/v1beta1"
    obj["kind"] = "TokenReview"
    obj["status"] = {}
    obj["status"]["authenticated"] = False
    return json.dumps(obj)


if __name__ == "__main__":
    app.run()
