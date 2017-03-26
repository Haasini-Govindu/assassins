from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from database import db
import sms
import web as web

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(application)

@application.route('/sms', methods=['POST'])
def root():
    return sms.handleSms(request)

@application.route("/")
def homepage():
	return web.homepage()

@application.route("/leaderboard/<code>")
def leaderboard(code):
	return web.leaderboard(code)

@application.route('/create')
def create_show():
	return web.create_show(None)

@application.route('/create/<code>')
def create_show_code(code):
	return web.create_show(code)

@application.route('/create', methods=['POST'])
def create_submit():
	return web.create_submit(request)
