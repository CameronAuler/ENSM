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
    properties = []
    for item in split_log:
        if split_log[split_log.index(item) + 1] == ":" and item not in properties:
            properties.append(item)
        else:
            pass
    return properties

def get_line(split_log, properties):
    
    property_entry = ""
    message = []
    for item in split_log:
        if item in properties:
            if split_log.index(item) > 0:
                property_entry += "," + item + ":"
            else:
                property_entry += item + ":"
        elif item == "Message":
            property_entry += "," + item
        elif item not in properties and item != ":":
            property_entry += item
        else:
            pass
        split_log.remove(item)
    return property_entry


def build():
    log = {}
    property_entry = ""
    is_data = False
    print(get_properties(result))
    print(get_line(result, get_properties(result)))

build()
# Write to file
#with open("logs.txt", "w") as file:
#    file.write(f"{item},")

# print(os.getcwd())
#print(os.listdir(os.getcwd()))
# print(os.getlogin())