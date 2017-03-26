from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from database import db
import sms
import web as web

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

@app.route('/sms', methods=['POST'])
def root():
    return sms.handleSms(request)

@app.route("/")
def homepage():
	return web.homepage()

@app.route("/leaderboard")
def leaderboard():
	return web.leaderboard()
