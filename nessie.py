# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
import nessie_auth	

class GameMaster:
	
	def __init__(self):
		self.apiKey = nessie_auth.getApiKey()
		self.customerId = nessie_auth.getCustomerId()
	
gm = GameMaster()
print 'API Key: ' + str(gm.apiKey)

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(gm.customerId,gm.apiKey)
payload = {
  "type": "Savings",
  "nickname": "test4",
  "rewards": 3,
  "balance": 1090,	
}
# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')
else:
	print('Status Code: ' + str(response.status_code))