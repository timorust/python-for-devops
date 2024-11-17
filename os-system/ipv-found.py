import os

ipv4_found = False

with os.popen("ipconfig") as cmd:
	for line in cmd:
		newLine = line.replace("\n", "")

		if "IPv4 Address" in newLine:
			ipv4_address = newLine.split(":")[-1].strip()
			print("IPv4 Address found:=> ", ipv4_address)

			ipv4_found = True
			break

if not ipv4_found:
	print("IPv4 Address not found")