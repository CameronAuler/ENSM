import socket
import subprocess
import threading

# GATHER LOGS WITH POWERSHELL COMMANDS
def gather_logs():
    # Commands
    # Get full log
    form = "Get-EventLog -LogName Security -Newest 1 | Format-List -Property * | out-host"
    # Get specific element of a log
    filter = "Get-EventLog -LogName Security -Newest 1 | Format-List -Property EventID | out-host"
    # Powershell admin command
    admin = "Start-Process powershell -Verb RunAs"

    # Retrieve the logs
    output = subprocess.Popen(
        ["powershell", "-Command", form],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        #shell=True,
        #capture_output=True,
        #text=True
        )
    
    output.poll()
    stdout, stderr = output.communicate()
    result = stdout.decode().split()
    return result


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

#print(log_list(gather_logs(), get_properties(gather_logs())))

# CONSTRUCT PACKET

# SOCKET CONNECTION
ADDRESS = "127.0.0.1"
PORT = 8888
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ADDRESS, PORT))

def receive():
    log_entries = log_list(gather_logs(), get_properties(gather_logs()))
    log_str = ""
    while True:
        try:
            for entry in log_entries:
                for item in entry:
                    log_str += f"{item},"
            client_socket.send(log_str.encode())
        except:
            print("An error occured!")
            client_socket.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()
    