from twilio import twiml
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def root():
	print(request.form['Body'])
	if(request.form['Body'].lower() == 'join'):
		return handle_join(request.form['From'])
	if(request.form['Body'].lower().split(' ')[0] == 'kill'):
		return handle_kill(request.form['From'], request.form['Body'].lower())
	return handle_idk()

def handle_join(sender):
	response = twiml.Response()
	if(in_game(sender)):
		response.message('you\'re already in a game!')
		return str(response)
	join_game(sender)
	target = get_target(sender)
	response.message('joined the game! your first target is ' + target)
	return str(response)
	
def handle_kill(sender, text):
	args = text.split(' ')
	response = twiml.Response()
	if(len(args) < 2):
		response.message('please include your victim\'s code')
		return str(response)
	if(kill(sender, args[1])):
		target = get_target(sender)
		response.message('successfull kill! your next target is ' + target)
		return str(response)
	response.message('sorry, but that code isn\'t right')
	return str(response)

def handle_idk():
	response = twiml.Response()
	response.message('what?')
	return str(response)


# placeholder functions
game = False

def in_game(sender):
	return game

def join_game(sender):
	global game
	game = True

def get_target(sender):
	return 'charlie'

def kill(sender, code):
	return code == 'yes'
