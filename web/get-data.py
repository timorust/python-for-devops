import urllib3

http = urllib3.PoolManager()

url = "http://www.google.com"

response = http.request("GET", url)
data = response.data.decode()

print(data)
response.close()
