import subprocess
import ctypes

def runCmd(*args):
    p = subprocess.Popen(
        *args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    out, error = p.communicate()
    return out, error

#commands = u'/k echo hi'
#ctypes.windll.shell32.ShellExecuteW(
#        None,
#        u"runas",
#        u"cmd.exe",
#        commands,
#        None,
#        1
#    )

#command = ['cmd.exe', '/c', 'runas', '/user:administrator', 'regedit']
#p = subprocess.Popen(command, stdin=subprocess.PIPE)
#p.stdin.write('password')
#p.communicate()

p = subprocess.Popen(
  [
    "powershell.exe", 
    "-noprofile", "-c",
    r"""
    Start-Process -Verb RunAs -Wait powershell.exe -Args "
      -noprofile -c Set-Location \`"$PWD\`"; & D:\Cyber_security\Python\login.ps1
      "
    """
  ],
  stdout=sys.stdout
)
p.communicate()



ps_command = "& {{Start-Process cmd.exe -argumentlist '/k \"dir\"' -Verb Runas}}"
command = ['powershell.exe', '-command', ps_command]
runCmd(command)