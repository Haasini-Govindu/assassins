# clearaccounts.py
# NOTE: This Python file serves no purpose outside of testing/development.

import requests
import json
import nessie_auth	

apiKey = nessie_auth.getApiKey()
customerId = nessie_auth.getCustomerId()
url = 'http://api.reimaginebanking.com/accounts?key={}'.format(apiKey)

response = requests.get(url, )

if response.status_code == 200:
	data = response.json()
	print('Retrieved All Accounts')
	
	accountIDs = []
	for account in data:
		delUrl = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(account['_id'], apiKey)
		delResponse = requests.delete(delUrl,)
		if delResponse.status_code == 204:
			print('Deleted ' + account['nickname'] + '\'s Account')
		else:
			print('Error Status Code: ' + str(response.status_code))
	
else:
	print('Error Status Code: ' + str(response.status_code))