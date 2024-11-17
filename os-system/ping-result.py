import os 

folderName = "ping_results"
os.mkdir(folderName)
os.chdir(folderName)

website = "www.google.com"
pingCommand = f"ping {website} > ping_results.txt"
os.system(pingCommand)

pingSuccessfully = False
with open("ping_results.txt", "r") as file:
    for line in file:
        newLine = line.replace("\n", "")
        if "Reply from" in newLine:  # תיקון למחרוזת הנכונה
            pingSuccessfully = True
            break

if pingSuccessfully:
    print("Ping successful connection is activated")
else:
    print("Ping failed connection is not activated")
