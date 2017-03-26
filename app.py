from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

from database import db
import sms
import web as web

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['FLASK_DB'] or 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

@app.route('/sms', methods=['POST'])
def root():
    return sms.handleSms(request)

@app.route("/")
def homepage():
	return web.homepage()

@app.route("/leaderboard/<code>")
def leaderboard(code):
	return web.leaderboard(code)

@app.route('/create')
def create_show():
	return web.create_show(None)

@app.route('/create/<code>')
def create_show_code(code):
	return web.create_show(code)

@app.route('/create', methods=['POST'])
def create_submit():
	return web.create_submit(request)
