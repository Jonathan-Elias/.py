from paramiko import SSHClient
import paramiko
import time


#Variáveis

host = ('xxx.xxx.xxx.xxx')
port = ('22')
username = ('xxxxx')
password = ('xxxxxxx')

#COMANDOS LINUX

commands = ('yum -y install httpd',
            'systemctl enable httpd',
            'systemctl start httpd',
            'systemctl status httpd',
            'cat /etc/*-release')

#CONFIGURAÇÂO SSH

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

for a in commands:
    stdin, stdout, stderr = ssh.exec_command(a.encode())
    time.sleep(.3)
    line = stdout.readlines()
    err = stderr.readlines()
    for a in line:
        print(a.replace('\n',''))
    print(err)
    print('\n')

ssh.close()


SAIR = input('\nPRESSIONE ENTER PARA SAIR!!!')
