import socket

HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

while True:
    message = input("Enter a message: ")

    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()

    print(response)

    if message == "exit":
        client_socket.close()
        break
