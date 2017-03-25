# clearaccounts.py
# NOTE: This Python file serves no purpose outside of testing/development.

import requests
import json
import nessie_auth	

apiKey = nessie_auth.getApiKey()
customerId = nessie_auth.getCustomerId()
url = 'http://api.reimaginebanking.com/accounts?key={}'.format(apiKey)

#'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId, apiKey)

# payload = {
# 	"type": "Checking",
# 	"nickname": assassin['Name'],
# 	"rewards": 0,
# 	"balance": 5,	
# }

response = requests.get(url, )

if response.status_code == 200:
	print('Retrieved All Accounts')
	data = response.json()
	accountIDs = []
	for account in data:
# 		accountIDs.append(account['_id'])
		delUrl = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(account['_id'], apiKey)
		delResponse = requests.delete(delUrl,)
		if delResponse.status_code == 204:
			print('Deleted ' + account['nickname'] + '\'s Account')
		else:
			print('Error Status Code: ' + str(response.status_code))
	
else:
	print('Error Status Code: ' + str(response.status_code))