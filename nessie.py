# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
import nessie_auth	

# GameMaster class for storing authentication related information for the duration of the game
class GameMaster:
	
	def __init__(self):
		self.apiKey = nessie_auth.getApiKey()
		self.customerId = nessie_auth.getCustomerId()
		self.url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(self.customerId, self.apiKey)
	
gm = GameMaster()

person1 = {
  "Name": "Ahri",
  "Phone Number": "+180022212222",	
}

person2 = {
  "Name": "Katarina",
  "Phone Number": "+180022212222",	
}

person3 = {
  "Name": "Kha'zix",
  "Phone Number": "+180022212222",	
}

person4 = {
  "Name": "Rengar",
  "Phone Number": "+180022212222",	
}

person5 = {
  "Name": "Talon",
  "Phone Number": "+180022212222",	
}

person6 = {
  "Name": "Zed",
  "Phone Number": "+180022212222",	
}

participants = [person1, person2, person3, person4, person5, person6]

payload = {
  "type": "Checking",
  "nickname": "test url change",
  "rewards": 3,
  "balance": 1090,	
}


# Create a Checking Account
response = requests.post( 
	gm.url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')
else:
	print('Error Status Code: ' + str(response.status_code))