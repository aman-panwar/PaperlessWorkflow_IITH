from flask import Flask, request, jsonify
from flask_cors import CORS
from Model.user import User
from Model.formMetaData import FormMetaData
from Controller.command import *

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
    data=request.json
    formdata=data["data"]
    form_type=data["form_type"]
    app_id=data["user"]["email"]
    form_meta=FormMetaData(form_type=form_type)
    fields=form_meta.get_level(0)[1]
    field_vals=[]
    for x in fields:
        field_vals.append(formdata[x[0]])
    val=Accept(_form_id=None,_user_id=app_id,_field_vals=field_vals).user_submit(form_name=form_type)
    response = {"success": val}
    return jsonify(response)


if __name__ == "__main__":
    app.run()
