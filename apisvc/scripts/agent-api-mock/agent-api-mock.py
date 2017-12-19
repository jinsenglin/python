from flask import Flask
app = Flask(__name__)

@app.route("/v1/healthz")
def healthz():
    return "ok"

@app.route("/v1/role/os", methods=['PUT'])
def role_os():
    return '{"status": 200}'

@app.route("/v1/role/k8s", methods=['PUT'])
def role_k8s():
    return '{"status": 200}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=40080, debug=True)
