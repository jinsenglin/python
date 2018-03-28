import json
from flask import Flask
from flask import request
from monascaclient.shell import main

app = Flask(__name__)

@app.route("/publish/", methods=['POST'])
def publish():
    for m in json.loads(request.data):
        if m['plugin'] == 'statsd' :
            ml = ['metric-create', '--time', str(m['time']*1000), str(m['type_instance']), str(m['values'][0])]
            main(ml)
    return "ok"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=50000)
