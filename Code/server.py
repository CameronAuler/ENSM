#server.py
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8000
ADDRESS = "0.0.0.0"
my_socket.bind((ADDRESS, PORT))
my_socket.listen()
client, client_address = my_socket.accept()
# Instead of receiving only one message, let's make an infinite loop
while True:
    result = client.recv(1024)
    print(result.decode())