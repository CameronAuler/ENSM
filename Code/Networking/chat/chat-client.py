import threading
import socket

nickname = input("Choose a username:")
ADDRESS = "127.0.0.1"
PORT = 8888
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ADDRESS, PORT))

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message =="cam":
                client_socket.send(nickname.encode())
            else:
                print(message)
        except:
            print("An error occured!")
            client_socket.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client_socket.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()