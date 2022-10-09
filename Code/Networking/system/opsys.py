import os
import subprocess

form = "Get-EventLog -LogName Security -Newest 5 | Format-List -Property * | out-host"
filter = "Get-EventLog -LogName Security | Select-Object EntryType, Message, Source, Subject"
filter2 = "Get-EventLog -LogName Security -Newest 20 | Select-Object EventID, MachineName, EntryType, Source | out-Host"

output = subprocess.run(["powershell", "-Command", filter2], capture_output=True)


result = output.stdout.decode()
print(result)

#with open("logs.txt", "w") as file:
#    file.write(result)

# print(os.getcwd())
#print(os.listdir(os.getcwd()))
# print(os.getlogin())