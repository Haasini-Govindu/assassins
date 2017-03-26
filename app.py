from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from targets import db
import sms

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

@app.route('/sms', methods=['POST'])
def root():
    return sms.handleSms(request)
