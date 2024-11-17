from bs4 import BeautifulSoup

import requests

inputDomainName = input("Please enter a domain name... ")
if not inputDomainName.startswith(("http://", "https://")):
	inputDomainName = "http://" + inputDomainName

response = requests.get(inputDomainName)
htmlDocument = response.text

soup = BeautifulSoup(htmlDocument, "html.parser")

divLink = soup.find("div")

linksTags = divLink.find_all("a")

for linkTag in linksTags:
	print("Link text is:=> " + linkTag.text, "URL:=> ", linkTag['href'])

