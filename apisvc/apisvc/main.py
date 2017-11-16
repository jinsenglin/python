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

if __name__ == "__main__":
    app.run()
