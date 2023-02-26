import socket
import threading

ADDRESS = "127.0.0.1"
PORT = 8888
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ADDRESS, PORT))
server_socket.listen(5)

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

# Encoding can be utf-8 or ascii

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nickname[index]
            broadcast(f"{nickname} left the chat!".encode())
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {str(address)}")
        name = "user"
        client.send(name.encode())
        
        nickname = client.recv(1024).decode()
        
        nicknames.append(nickname)
        clients.append(client)
        
        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode())
        client.send("Connected to the server!".encode())
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening . . .")
receive()