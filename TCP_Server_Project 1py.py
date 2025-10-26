#Gurvir Shergill, ID#000862625

#TCP Server
#Chosen Application: Echo App

#Import Libraries
from socket import *
import sys

#Socket Port#
svr_port = 500
#Opening the server socket
svr_socket = socket(AF_INET, SOCK_STREAM)

#Srver binds to the port and starts listening for requests
svr_socket.bind(('', svr_port))
svr_socket.listen(1)

#Server prints a message to show its ready
print('The server is ready to receive')

#Counter loop for timeout for exception handling
counter = 0

while counter < 1:
    print('Waiting...')
    connect_socket, clientAddress = svr_socket.accept()
    connect_socket.settimeout(10)

    try:
        #Start recieving and sending messages between client
        message = connect_socket.recv(1024).decode()
        connect_socket.send(message.encode())
        print('Message from Client: ', clientAddress)
        print('---------------------------------------')
        print(message)

    except timeout:
        counter += 1
        print ('Timeout')

    connect_socket.close()
sys.exit(0)

