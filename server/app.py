from flask import Flask
app = Flask(__name__)

@app.route("/contri") 
def index():
    return {
        "project": "SOAP",
        "contributer": ["aman", "ojas", "shreya", "pranav"]
        }

if __name__ == "__main__":
    app.run(debug=True)