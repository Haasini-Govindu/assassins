# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
import nessie_auth	

# GameMaster class for storing authentication related information for the duration of the game
class MasterAccount:
	
	def __init__(self, buyIn):
		self.apiKey = nessie_auth.getApiKey()
		self.customerId = nessie_auth.getCustomerId()
		self.url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(self.customerId, self.apiKey)
		self.buyIn = buyIn
	
	def createAccount(self, name):
		payload = {
			"type": "Checking",
			"nickname": name,
			"rewards": 0,
			"balance": self.buyIn,	
		}

		# Create a Checking Account
		response = requests.post( 
			self.url, 
			data=json.dumps(payload),
			headers={'content-type':'application/json'},
		)

		if response.status_code == 201:
			print('Account Created')
			data = response.json()
			return data['objectCreated']['_id']
		else:
			print('Error Status Code: ' + str(response.status_code))	
	
	def transfer(self, payer, assassin):
		tURL = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(payer, self.apiKey)
		
		payload = {
  			"medium": "balance",
  			"payee_id": assassin.get_id(),
  			"amount": self.buyIn,
  			"transaction_date": "2017-03-25",
  			"description": ("Loot from")
		}
		
		response = requests.post(
			tURL,
			data=json.dumps(payload),
			headers={'content-type':'application/json'}
		)
		
		if response.status_code == 201:
			print('Transfer Complete')
			print response.json()
		else:
			print('Error Status Code: ' + str(response.status_code))
			
	def getBalance(self, player):
		pURL = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(player, self.apiKey)
		response = requests.get(pURL)
		
		if response.status_code == 200:
			print('Successfully obtained account balance')
			data = response.json()
			bal = float(data['balance'])
			return bal
# 			print data
# 			return 5
		else:
			print('Error Status Code: ' + str(response.status_code))
				
# participants = [person1, person2, person3, person4, person5, person6]
# 
# for assassin in participants:
# 	payload = {
# 		"type": "Checking",
# 		"nickname": assassin['Name'],
# 		"rewards": 0,
# 		"balance": 5,	
# 	}
# 
# 	# Create a Checking Account
# 	response = requests.post( 
# 		gm.url, 
# 		data=json.dumps(payload),
# 		headers={'content-type':'application/json'},
# 		)
# 
# 	if response.status_code == 201:
# 		print('account created')
# 	else:
# 		print('Error Status Code: ' + str(response.status_code))
