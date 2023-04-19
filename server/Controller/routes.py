import os 
import sys


filePath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, filePath)

from Model.user import User
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/form/submit', methods=['POST'])
def handle_submit():
    newUser = User()


    name = request.form['name']
    email = request.form['email']
    dob = request.form['dob']

    data = {"name": name, "email": email, "dob": dob}
    newUser.addInfo(data)
    print(newUser)
    print(newUser.name + '\n' + newUser.email + '\n' + newUser.dob)

    return "ADDED USER"

if __name__ == "__main__":
    app.run()
