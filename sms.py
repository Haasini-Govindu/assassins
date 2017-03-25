from twilio import twiml
from flask import Flask, request

# import targets
from targets import Player, Game


app = Flask(__name__)

game = Game()

awaitingResponse = {}

@app.route("/", methods=['GET', 'POST'])
def root():
	print(request.form['Body'])

	# debug
	if(request.form['Body'] == 'debug'):
		game.printStatus()

	if(request.form['From'] in awaitingResponse):
		return awaitingResponse.pop(request.form['From'])(request)
	body = request.form['Body'].lower().strip()
	if(body == 'start'):
		return handleStart()
	if(body == 'join'):
		return handleJoin(request.form['From'])
	if(body.split(' ')[0] == 'kill'):
		return handleKill(request.form['From'], body)
	if(body == 'leaderboard'):
		return handleLeaderboard()
	return handleIdk()

def getName(request):
	game.addPlayer(Player(request.form['Body'], request.form['From']))
	
	response = twiml.Response()
	response.message('you joined the game! we\'ll let you know when it starts')
	return str(response)

def handleStart():
	game.start()
	response = twiml.Response()
	response.message('all players have been notified of the game start')
	return str(response)

def handleJoin(sender):
	response = twiml.Response()
	if(game.findPlayer(sender)):
		response.message('you\'re already in a game!')
		return str(response)
	awaitingResponse[sender] = getName
	response.message('what\'s your name?')
	return str(response)
	
def handleKill(sender, text):
	args = text.split(' ')
	response = twiml.Response()
	if(len(args) < 2):
		response.message('please include your victim\'s code')
		return str(response)
	player = game.findPlayer(sender);
	if(not(player)):
		response.message('you\'re not even playing dumbass')
		return str(response)
	if(game.assassinationAttempt(player, args[1])):
		target = player.getTarget()
		response.message('successfull kill! your next target is ' + target)
		return str(response)
	response.message('sorry, but that code isn\'t right')
	return str(response)

def handleIdk():
	response = twiml.Response()
	response.message('what?')
	return str(response)

def handleLeaderboard():
	response = twiml.Response()
	response.message(game.leaderboard())
	return str(response)


# placeholder functions
ingame = False

def inGame(sender):
	return ingame

def joinGame(sender, name):
	global ingame
	ingame = True

def getTarget(sender):
	return 'charlie'

def kill(sender, code):
	return code == 'yes'
