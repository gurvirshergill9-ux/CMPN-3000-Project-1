import sys
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
serverSocket.settimeout(10)

print('The server is ready to receive')
counter = 0

while counter < 1:
    print('Waiting...')
    message, clientAddress = serverSocket.recvfrom(1024)
    
    try:
        print('Connected to: ', clientAddress)
        modifiedMessage = message.decode()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        
        print('Message from Client: ', clientAddress)
        print('-------------------------------------------------------')
        print(modifiedMessage)

    except timeout:
        counter += 1
        print ('Timeout')

    serverSocket.close()
sys.exit(0)
    
    
