#!/root/anaconda3/bin/python3

import time
import datetime

from paramiko import SSHClient
import paramiko

#SSH configuration

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Variables

ip = "177.69.107.40"
user = "root"
password = "#19Tes90#"

timeOpen = datetime.time(8, 0, 0) #(hour, minute, seconds)
timeClose = datetime.time(18, 0, 0)

commandsOpen = [
    "systemctl start httpd",
    "clear"
    ]

commandsClose = [
    "systemctl stop httpd",
    "clear"
]

def start():
    '''
        get varibles values for login
    '''
    global ip, user, password

    print("Entre com IP: ", end="")
    ip = input()
    print("Entre com Usuário: ", end="")
    user = input()
    print("Entre com Senha: ", end="")
    password = input()

def openSSH():
    ssh.connect(
        hostname=ip,
        port=22,
        username=user,
        password=password
    )

def printOut(s):
    print(str(s).replace("\\n", "\n").replace("\\r", "\r"))

#Criar Shell



#Comandos

#comandos para switch = [
#    "enable",
#    " conf t",
#    "int gi 1/0/6",
#    "no shut"
#    ]

#comandos para servidor Linux CentOS
def runCommands(commands):

    #Open Shell

    shell = ssh.invoke_shell()
    time.sleep(.5)
    printOut(shell.recv(65535))

    #Execute commands

    for command in commands:
        shell.send(command + "\n") # executar comando
        time.sleep(.5) # esperar 0.5 segundos
        printOut(shell.recv(65535)) # print saida
        print("#########################################\n")

'''
entrada, saida, error =  ssh.exec_command(comando)

if error.channel.recv_exit_status() == 0:
    print(saida.read())
else:
    print(error.read())'''

def closeSSH():
    ssh.close()

#Flow

#start()

wasCommandsRunned = False

while True:	
    now = datetime.datetime.now().time()
    #print(now)

    if not wasCommandsRunned:
        #Open
        if now >= timeOpen:
            print("Opening")
            openSSH()
            runCommands(commandsOpen)
            closeSSH()
            wasCommandsRunned = True
    else:
        #Close
        if now >= timeClose:
            print("Closing")
            openSSH()
            runCommands(commandsClose)
            closeSSH()
            break;

    time.sleep(1)

print("end")