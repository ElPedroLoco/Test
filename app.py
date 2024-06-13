from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Imagine fetching data from a database or performing some calculations
    data = {'value': 42}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
