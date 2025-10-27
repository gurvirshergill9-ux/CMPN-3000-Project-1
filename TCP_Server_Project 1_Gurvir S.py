#Gurvir Shergill, ID#000862625

#TCP Server
#Chosen Application: Echo App

#References: In class notes (Weeks 1-7) and labs


#Import Libraries
from socket import *
import sys

#Socket Port#
svr_port = 500
#Opening the server socket
svr_socket = socket(AF_INET, SOCK_STREAM)

#Server binds to the port and starts listening for requests
svr_socket.bind(('', svr_port))
svr_socket.listen(1)

#Server prints a message to show its ready
print('The server is ready to receive')

#Counter loop and timeout for exception handling
count = 0
svr_socket.settimeout(10)

#Server will attempt to make 2 connections before timeout
while count < 2:
    print('Waiting...')
    
    #Accept connection funtion
    connect_socket, client_address = svr_socket.accept()

    try:
        #Start recieving and sending messages between client
        message = connect_socket.recv(1024).decode()
        connect_socket.send(message.encode())
        
        #Prints client output along with address
        print('Message from Client: ', client_address)
        print('---------------------------------------')
        print(message)

    except timeout:
        #Exception after 10 seconds
        count += 1
        print ('Timeout')

    #Close the socket
    connect_socket.close()

    #Close the program
    sys.exit(0)

