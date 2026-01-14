from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    return jsonify({"prediction": "success", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
