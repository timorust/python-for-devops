def handle_commands(client_socket, server_socket):
    while True:
        try:
            # Receiving a command from a user
            command = input("Enter the command for the client... ")

            if command.lower() == "exit":
                # server encode and sends it to the client.
                client_socket.send(command.encode())
                print("[+] Close connection...")
                break

            # Sending a command to the client
            client_socket.send(command.encode())

            # Receiving a response from the client
            result = client_socket.recv(1024).decode()
            print(f"Result of execution:=> \n{result}")
        except Exception as e:
            print(f"[!] Error: {e}")
            break

    client_socket.close()
    server_socket.close()
