import urllib3

isinstanceModel = urllib3.PoolManager()

pages = ["car", "bla", "index", "login", "robots.txt", "Home"]

for page in pages:
	response = isinstanceModel.request("GET", f"https://hack-yourself-first.com/{page}")
	if response.status == 200:
		print(f"Page found:=> https://hack-yourself-first.com/{page}")
	else:
		response = isinstanceModel.request("POST", f"https://hack-yourself-first.com/{page}")
		if response.status == 200:
			print(f"Page found:=> https://hack-yourself-first.com/{page} with POST request")
		else:
			print(f"Page not found for both GET and POST: https://hack-yourself-first.com/{page}")
