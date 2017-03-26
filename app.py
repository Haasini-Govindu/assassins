from flask import Flask, request

import sms

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def root():
    return sms.handleSms(request)
