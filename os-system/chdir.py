import os
if not os.path.exists("newfolder"):
	os.mkdir("newfolder")
	os.chdir("newfolder")

print(os.getcwd())	