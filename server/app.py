from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/contri") 
def index():
    return {
        "project": "SOAP",
        "contributer": ["aman", "ojas", "shreya", "pranav"]
        }

if __name__ == "__main__":
    app.run(debug=True)