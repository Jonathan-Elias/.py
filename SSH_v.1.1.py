#!/usr/bin/pyhton3

from paramiko import SSHClient
import paramiko

#Variáveis

host = input('Insira o IP: ')
port = 22
username = input('Insira o Usuário: ')
password = input('Insira a Senha: ')

#COMANDOS LINUX

commands = ('nmcli device show')

#CONFIGURAÇÂO SSH

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(commands)
lines = stdout.readlines()
print(lines)
