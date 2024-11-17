import urllib3

http = urllib3.PoolManager()

url = "http://example.com/notexist"

response = http.request("GET", url)

if response.status == 404:
	print("Error 404: Page not fount")
else:
	print("Successfully!! page found")	