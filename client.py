from socket import *
HOST = 'localhost'
PORT = 28812
BUFSIZE = 1024
ADDR = (HOST, PORT)
f=open("msg.txt","r")
tcpTimeClientSock = socket(AF_INET, SOCK_STREAM)
tcpTimeClientSock.connect(ADDR)
while True:
  data = f.readline()
  if not data:
      break
  tcpTimeClientSock.send(data)
  data = tcpTimeClientSock.recv(BUFSIZE)
  if not data:
      break
print data
tcpTimeClientSock.close()
f.close()
