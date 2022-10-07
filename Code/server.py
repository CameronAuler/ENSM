
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection information
server_port = 8000
server_address = "10.0.0.215"

# The following line of code retrieves the IP of the system it is on automatically, but doesn't work with VM initialization
'''
ADDRESS = socket.gethostbyname(socket.gethostbyname())
'''

# Bind the port and address
socket.bind((server_address, server_port))

# Initiate listening on server
# Restricts the number of connections with the 5(ignores excess connection requests)
server_socket.listen(5)

# Comm_socket is another socket for communication on the server, the server_socket only accepts connections.
while True:
    comm_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")
    
    # 1024 is the buffer size in bytes
    message = comm_socket.recv(1024).decode('utf-8')
    print(f"Message from client --> {message}")
    comm_socket.send(f"server has recieved your message!".encode('utf-8'))
    comm_socket.close()
    print(f"connection with {client_address} terminated!")