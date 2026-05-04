
from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Model Running 🚀"

@app.route("/predict", methods=["GET"])
def make_prediction():
    value = request.args.get("value", type=int)
    if value is None:
        return jsonify({"error": "Provide value"}), 400

    result = predict(value)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
