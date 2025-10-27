#Gurvir Shergill, ID#000862625

#UDP Server
#Chosen Application: Echo App

#References: In class notes (Weeks 1-7) and labs

#Import Libraries
import sys
from socket import *

#Socket Port#
svr_port = 12000
#Opening the server socket
svr_socket = socket(AF_INET, SOCK_DGRAM)

#Server binds to the port
svr_socket.bind(('', svr_port))

#Server prints a message to show its ready
print('The server is ready to receive')

#Server prints a message to show its ready
count = 0
svr_socket.settimeout(10)

#Server will attempt to make 3 connections before timeout
while count < 2:
    print('Waiting...')

    try:
        #Start recieving and sending messages between client
        message, client_address = svr_socket.recvfrom(1024)
        modmessage = message.decode()
        svr_socket.sendto(modmessage.encode(), client_address)
        
        #Prints client output along with address
        print('Message from Client: ', client_address)
        print('---------------------------------------')
        print(modmessage)
    
    #Exception after 10 seconds
    except timeout:
        count += 1
        print ('Timeout')
    
    #Close the socket
    svr_socket.close()

    #Close the program
    sys.exit(0)
    
    
