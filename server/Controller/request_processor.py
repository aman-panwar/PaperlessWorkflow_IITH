from flask import Flask, json, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/get_process', methods=['GET'])
def handle_get():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    print("Entered get processor")

    response_data = {
        'message': 'FLASK GET HELLO',
        'param1': param1 + ' FLASK',
        'param2': param2 + ' FLASK',
    }

    return jsonify(response_data)

@app.route('/post_process', methods=['POST'])
def handle_post():
    param1 = request.form['param1']
    param2 = request.form['param2']
    print("Entered POST processor")

    response_data = {
        'message': 'FLASK POST HELLO',
        'param1': param1 + ' FLASK',
        'param2': param2 + ' FLASK',
    }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host='localhost', port=8000)
