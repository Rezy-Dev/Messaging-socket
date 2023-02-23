import socket

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()

print("Server is waiting for incoming connections...")
client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established!")

while True:
    message = client_socket.recv(1024).decode()

    if not message:
        print(f"{address} has disconnected.")
        break

    print(f"Received message from {address}: {message}")
    response = f"Received message: {message}"
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()
