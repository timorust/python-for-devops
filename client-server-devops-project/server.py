import socket
from command_handler import handle_commands

# Initializing the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'  # Local IP
PORT = 65432        # Server port
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("[+] The server is ready to accept connections")

# Waiting for client connection
client_socket, client_address = server_socket.accept()
print(f"[+] Connection established with:=> {client_address}")

# Command processing
handle_commands(client_socket, server_socket)
