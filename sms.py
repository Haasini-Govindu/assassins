from twilio import twiml
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    response = twiml.Response()
    print(request.form['Body'])
    response.message("got it, thanks!")
    return str(response)
