import socket
import threading

ADDRESS = "127.0.0.1"
PORT = 8888
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ADDRESS, PORT))
server_socket.listen(5)

clients = []

# FORMAT LOGS FOR DATA TRANSFER
# Gather the properties/headers of the log
def get_properties(split_log):
    property_places = []
    for item in split_log:
        if split_log[split_log.index(item) + 1] == ":":
            property_places.append(split_log.index(item))
        else:
            pass
    return property_places

# Format the log into a list split up by properties/headers
def log_list(split_log, places):
    log = []    
    for item in places:            
        if places.index(item) > 0 and places.index(item) != len(places) - 1:
            log.append(split_log[places[places.index(item) - 1]:item])
            
        elif places.index(item) == len(places) - 1:
            log.append(split_log[places[places.index(item) - 1]:item])
            log.append(split_log[item:len(split_log)])
        else:
            pass
    return log

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
            break

def receive():
    log_str = ""
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {str(address)}")
    
        log = client.recv(1024).decode()
        log_str += log
        log_split = log_str.split(",")
        log = log_list(log_split, get_properties(log_split))
        print(log)
        #print(type(log))
        clients.append(client)
        
        #print(f"Nickname of the client is {nickname}!")
        #broadcast(f"{nickname} joined the chat!".encode())
        client.send("Connected to the server!".encode())
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening . . .")
receive()