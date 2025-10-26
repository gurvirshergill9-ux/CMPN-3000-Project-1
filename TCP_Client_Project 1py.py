#Gurvir Shergill, ID#000862625

#TCP Client
#Chosen Application: Echo App

#Import Libraries
from socket import *
import sys

#Client Socket Port and Address
server_addr = '192.168.1.73'
svr_port = 500
#Opening the client socket
cln_socket = socket(AF_INET, SOCK_STREAM)

#Client connects to the server by entring the server IP server Port 
cln_socket.connect((server_addr, svr_port))

#User input for message to be sent to server
message = input('Enter Message: ')
#Clint starts sending message to srver
cln_socket.send(message.encode())

#Client recives a request from the server and prints it out
modifiedMessage = cln_socket.recv(1024)
print ('Output from Server:', modifiedMessage.decode())

#Counter for tiemout exception handling
counter = 0

try:
    #Final message from server before disconnection
    ems = cln_socket.recv(1024).decode()
    print (ems)
    cln_socket.close()
    
except timeout:
    print('Timeout')
    counter += 1
    #Close the socket
    cln_socket.close()

