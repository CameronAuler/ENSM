import socket

ADDRESS = "127.0.0.1"
PORT = 8888
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ADDRESS, PORT))
server_socket.listen(5)

while True:
    client_socket, client_ADDRESS = server_socket.accept()