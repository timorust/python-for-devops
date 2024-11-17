import os

folderName = "list-folder"

os.makedirs(folderName, exist_ok=True)

os.chdir(folderName)

folderContents = os.listdir()

print("Contents of:=> ", folderName + ":")

for item in folderContents:
	print(item)