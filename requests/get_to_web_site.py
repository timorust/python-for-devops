import requests

response = requests.get('https://timorust.github.io/portfolio/')
print(response.status_code)
print(response.text)