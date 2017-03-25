from twilio.rest import TwilioRestClient
import twilio_auth

client = TwilioRestClient(twilio_auth.getSid(), twilio_auth.getAuthToken())

def killed(player):
	body = 'you were killed. you final balance was $' + str(10)
	message = client.messages.create(body=body, to=player.number, from_=twilio_auth.getNumber())

def start(player):
	body = 'the game begins!'
	client.messages.create(body=body, to=player.number, from_=twilio_auth.getNumber())
	body = 'your target is ' + player.target.getName()
	client.messages.create(body=body, to=player.number, from_=twilio_auth.getNumber())
	body = 'your secret code is ' + player.secretCode
	client.messages.create(body=body, to=player.number, from_=twilio_auth.getNumber())

def gameover(player, winner):
	body = winner.getName() + ' has won the game!'
	client.messages.create(body=body, to=player.number, from_=twilio_auth.getNumber())
