from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/form/submit', methods=["POST"])
def handle_submit():
    return ''

@app.route('/form/approve', methods=["POST"])
def handle_approve():
    return ''

@app.route('/form/reject', methods=["POST"])
def handle_reject():
    return ''

@app.route('/form/review', methods=["POST"])
def handle_review():
    return ''

@app.route('/form/render', methods=["GET"])
def handle_render():
    return ''
