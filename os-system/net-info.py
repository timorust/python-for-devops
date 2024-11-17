import os

os.system("ping 8.8.8.8 > ping_output.txt")

os.system("ipconfig > ipconfig_output.txt")

os.system("tracert www.google.com > tracert_output.txt")

for filename in ["tracert_output.txt", "ipconfig_output.txt", "ping_output.txt"]:
	print(f"Contents of {filename} is: => ")

	with open(filename, 'r') as file:
		print(file.read())
print("======================================")		
