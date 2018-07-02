from socket import *
clientPort=12000
clientName='localhost'
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((clientName,clientPort))
sentence=b'fsdfs'
clientSocket.send(sentence)
clientMessage=clientSocket.recv(1024)
print (clientMessage)
clientSocket.close()

