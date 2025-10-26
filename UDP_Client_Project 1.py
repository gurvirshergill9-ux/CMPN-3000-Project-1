import sys
from socket import *
serverName = '192.168.1.73'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Enter Message: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
print('Output from Server: ', modifiedMessage.decode())
clientSocket.close()
sys.exit(0)
