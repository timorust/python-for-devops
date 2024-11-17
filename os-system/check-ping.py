import os

file = open("ping_store.txt", "r")

for line in file:
	newLine = line.replace('\n', '')
	if "ms" in newLine:
		print(f"The connection succeeded")
		break
print("End")
