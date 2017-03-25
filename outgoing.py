from twilio.rest import TwilioRestClient
import twilio_auth

print(twilio_auth.getSid())
print(twilio_auth.getAuthToken)
client = TwilioRestClient(twilio_auth.getSid(), twilio_auth.getAuthToken())

def killed(to):
	money = get_balance(to);
	message = client.messages.create(body='you were killed. you final balance was $' + str(money),
									 to=to,
									 from_=twilio_auth.getNumber())

	print(message.sid)
	


# placeholder functions
def get_balance(to):
	return 10

killed('+17652336222')
