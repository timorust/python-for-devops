import os

try:
	with open("ping_store.txt", "w") as file:
		pass

	os.system("ping 8.8.8.8 > ping_store.txt")

except	IOError as e:
	print(f"Error:=> {e.strerror}")