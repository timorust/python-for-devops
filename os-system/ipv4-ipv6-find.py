import os
# print(os.environ)

result_file = "ipconfig_results.txt"

os.system(f'ipconfig > {result_file}')

try:
	with open(result_file, 'r') as file:
		ipv4_found = False
		ipv6_found = False
		for line in file:
			if "IPv4 Address" in line:
				ipv4_address = line.split(":")[-1].strip()
				print("IPv4 Address is:=> ", ipv4_address)
				ipv4_found = True
			elif "IPv6 Address" in line and not "Temporary" in line:
				ipv6_address = line.split(":")[-1].strip()	
				print("IPv6 Address is:=> ", ipv6_address)
				ipv6_found = True

		if not ipv4_found:
			print("IPv4 Address is not found")
		if not ipv6_found:
			print("IPv6 Address is not found")			
finally:
	os.remove(result_file)