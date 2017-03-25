# MHacks9
Project Repo for work done at MHacks 9 (University of Michigan, March 24-26, 2017)
Program to make organizing and running the classic "Assassins" game more fluid and efficient. 

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

# Dependencies
**requests**
On a command line, type in:
```bash
pip install requests
```

# Running flask server
```bash
export FLASK_APP=sms.py
export FLASK_DEBUG=1
flask run
```
