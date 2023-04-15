from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/async/get', methods=['GET'])
def handle_get():
    return jsonify({'message': 'Async get works!'})

@app.route('/async/post', methods=['POST'])
def handle_post():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Async post works!'})

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
