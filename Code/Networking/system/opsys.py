import os
import subprocess
from rich import inspect

# To Do
# - Determine how many properties a log has

# Commands
# Get full log
num = 2
form = "Get-EventLog -LogName Security -Newest 1 | Format-List -Property * | out-host"
test = "Get-EventLog -LogName Security -Newest 1 | Format-List -Property | out-host"
form2 = "Get-EventLog -LogName Security -Newest 1 | Format-List"

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

log = []

def build():
    property_entry = ""
    is_data = False
    for item in result:
        if item == ":" and item != result[0]:
            property_entry += result[result.index(item) - 1]
            is_data = True
            print(property_entry)
        elif  not is_data:
            property_entry = ""
        else:
            property_entry += item

build()
# Write to file
#with open("logs.txt", "w") as file:
#    file.write(f"{item},")

# print(os.getcwd())
#print(os.listdir(os.getcwd()))
# print(os.getlogin())