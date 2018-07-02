from socket import *
serverName='localhost'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
message =b'fsd'
clientSocket.sendto(message,(serverName,serverPort))
serverMessage,serverAddress=clientSocket.recvfrom(2048)
print(serverMessage)
clientSocket.close()

