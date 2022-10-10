import os
import subprocess
from rich import inspect

# To Do
# - Determine how many properties a log has

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

#print(dir(output), sep="\n")
#inspect(output)

result = stdout.decode().split()
#print(result)

# Print the Arguments passed to output
# print(dir(output), sep="\n")


def get_properties(split_log):
    prpoerty_places = []
    for item in split_log:
        if split_log[split_log.index(item) + 1] == ":":
            prpoerty_places.append(split_log.index(item))
        else:
            pass
    return prpoerty_places

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

print(log_list(result, get_properties(result)))

# Write to file
#with open("logs.txt", "w") as file:
#    file.write(f"{item},")

# print(os.getcwd())
#print(os.listdir(os.getcwd()))
# print(os.getlogin())