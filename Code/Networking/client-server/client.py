import socket

server_port = 8000
server_address = "10.0.0.215"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_address, server_port))

client_socket.send(f"testing client --> server {server_address} connection.".encode('utf-8'))
print(client_socket.recv(1024))