from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/api/v1/health")
def health():
    return jsonify({"success": True})

@app.route("/api/v1/auth", methods=["GET", "POST"])
def auth():
    return jsonify({"method": request.method})
if __name__ == "__main__":
    print("Hello world!")
