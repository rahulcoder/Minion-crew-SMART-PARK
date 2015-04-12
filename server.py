from socket import *
from time import ctime
HOST = 'localhost'
PORT = 28812
BUFSIZE = 1024
ADDR = (HOST, PORT)
#f=open("data.txt","w")
tcpTimeSrvrSock = socket(AF_INET,SOCK_STREAM)
tcpTimeSrvrSock.bind(ADDR)
tcpTimeSrvrSock.listen(50)

while True:
  #f=open("data.txt","w")
  print 'waiting for connection...'
  tcpTimeClientSock, addr = tcpTimeSrvrSock.accept()
  print '...connected from:', addr

  while True:
    f=open("data.txt","a")
    data = tcpTimeClientSock.recv(BUFSIZE)
    if not data:
      break
    data = data.strip()
    if data!=" ":
    	f.write(data)
    	print data
	f.close()
    tcpTimeClientSock.send('[%s] %s' % (ctime(), data))
    
  tcpTimeClientSock.close()
tcpTimeSrvrSock.close() 

