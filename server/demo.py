from flask import Flask, request, jsonify
from flask_cors import CORS
from Model.user import User

app = Flask(__name__)
CORS(app)

@app.route('/login/fetch_data', methods=['GET'])
def fetch_data(): 
    email = str(request.args.get('email'))
    logged_in_user = User(email=email)
    pending_forms = logged_in_user.pending_forms
    response_data = {'pending_forms': pending_forms}
    return jsonify(response_data)

@app.route('/demo/submit', methods={"POST"})
def demo_submit():
    data = request.get_json()
    print(data)
    return('200 OK')


if __name__ == "__main__":
    app.run()
