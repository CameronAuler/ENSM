import os
import time
import socket

ADDRESS = "127.0.0.1"
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ADDRESS, PORT))
server_socket.listen()

# Try to connect to socket
try:
    server_socket.connect((ADDRESS, PORT))
    print("Connected Successfully")
except:
    print("Unable to Connect")

# Receiving file deatils
file_name = server_socket.recv(100).decode()
file_size = server_socket.recv(100).decode()

# Open and writing the file
with open(file_name, "wb") as file:
    c = 0
    # Start Timer
    start_time = time.time()
    
    # Will run the loop till all of the file is received
    while c <= int(file_size):
        data = server_socket.recv(1024)
        if not (data):
            break
        file.write(data)
        c+= len(data)
    
    # End Timer
    end_time = time.time()
    
    print(f"File transfer is complete. Total time : {end_time - start_time}")
    server_socket.close()





'''
client, addr = server_socket.accept()

file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode()
print(file_size)

file = open(file_name, "wb")
file_bytes = b""

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data

file.write(file_bytes)
file.close()
client.close()
server_socket.close()
'''