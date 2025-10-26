#Gurvir Shergill, ID#000862625

#UDP Server
#Chosen Application: Echo App

#References: In class notes (Weeks 1-7) and labs

#Import Libraries
import sys
from socket import *

#Socket Port#
serverPort = 12000
#Opening the server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

#Server binds to the port
serverSocket.bind(('', serverPort))

#Server prints a message to show its ready
print('The server is ready to receive')

#Server prints a message to show its ready
counter = 0
serverSocket.settimeout(10)

#Server will attempt to make 3 connections before timeout
while counter < 3:
    print('Waiting...')

    try:
        #Start recieving and sending messages between client
        message, clientAddress = serverSocket.recvfrom(1024)
        modifiedMessage = message.decode()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        
        #Prints client output along with address
        print('Message from Client: ', clientAddress)
        print('---------------------------------------')
        print(modifiedMessage)
    
    #Exception after 10 seconds
    except timeout:
        counter += 1
        print ('Timeout')
    
    #Close the socket
    serverSocket.close()

    #Close the program
    sys.exit(0)
    
    
