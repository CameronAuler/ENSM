import os
import socket
import time

ADDRESS = "10.0.0.78"
PORT = 8888

# Creating the socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((ADDRESS, PORT))
client_socket.listen(5)

# Accept connection from client
client, addr = client_socket.accept()

# Getting file details
test = "test.txt"
file_name = test
file_size = os.path.getsize(test)

client.send(file_name.encode())
client.send(str(file_size).encode())

# Open and reading file
with open(file_name, "rb") as file:
    c = 0
    
    # Start Timer
    start_time = time.time()
    
    # Will run the loop till all of the file is sent
    while c <= int(file_size):
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c += len(data)
        
        file.write(data)
        c+= len(data)
    
    # End Timer
    end_time = time.time()

print(f"File transfer complete. Total time{end_time - start_time}")


# file.close()
client.close()