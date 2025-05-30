import joblib
import re
import sklearn
from flask import Flask 
from flask import render_template , request  , jsonify
from text_prediction.model import predict_

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/test')
def testing():
    return render_template("index_1.html")


@app.route('/classification', methods=['POST'])
def classify():

    data = request.form
    email_body = data.get("email_body")

    if not email_body:
        email_body = request.args.get("email_body")

    if not email_body:
        return jsonify({"error": "Missing email_body parameter"}), 400

    return jsonify({"prediction": predict_(email_body)})





if __name__ == '__main__':

    app.run(debug = True)