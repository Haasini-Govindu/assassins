# MHacks9
Project Repo for work done at MHacks 9 (University of Michigan, March 24-26, 2017)

# About the Hack  
Program primarily built in Python to make organizing and running the classic "Assassins" game more fluid and efficient.
Utilizes the Twilio API for communicating between players, as well as Capital One's Nessie API for tracking each assassin's financial accounts. 

# About the Game  
Players text in to join a game of assassins. Each player is assigned a "target" and subsequently are also being targeted, as well as a secret code.
Enter in your target's secret code on your own phone to verify your success, as well as obtain your next target.
Players who successfully assassinate their targets will take over their target's target until either time runs out or there is only one assassin left. 
Each player starts with their "buy in" amount in their bank account (auto generated during the start of the game). 
Eliminated assassins automatically have their initial buy in transferred to their killer. Thus, the Capital One bank accounts also double as a way of tracking the number of kills each player has.

# Disclaimer
While the rules of the physical game is up to the discretion of the participants, please keep in mind that it is still just a game. 
We do not encourage nor are we accountable for any injuries or even deaths resulting from participating in this activity. Do not perform a literal assassination on your target.

# APIs Utilized
[**Capital One's Nessie API**](api.reimaginebanking.com)  
[**Twilio API**](https://www.twilio.com/docs/)

# Hidden Files
**nessie_auth.py**  
Authentication information stored in a python file.
Hidden for security purposes.
```python
apiKey = '<api key here>'
customerId = '<customer id here>'

def getApiKey():
	return apiKey
	
def getCustomerId():
	return customerId
```

**twilio_auth.py**  
Same as `nessie_auth.py` but for twilio auth info.
These can be found on the Twilio console page
```python
account_sid = '<twilio accound SID here>'
auth_token = '<twilio auth token here>'
number = '+11234567890' #outgoing SMS number

def getSid():
	return account_sid
	
def getAuthToken():
	return auth_token

def getNumber():
	return number
```

# Dependencies
[**requests** (HTTP Library for Python)](http://docs.python-requests.org/en/master/user/install/)  
To install, run the following command:
```bash
pip install requests
```
Note that you may need to install pip beforehand if you have not yet already.

# Running flask server
```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```
