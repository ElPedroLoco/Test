from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict_client', methods=['POST'])
def predict_client():
    data = request.get_json()
    return jsonify({"status": "success", "data_received": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make Flask accessible from all IPs
