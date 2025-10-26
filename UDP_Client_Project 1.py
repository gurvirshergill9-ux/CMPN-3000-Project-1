#Gurvir Shergill, ID#000862625

#UDP Client
#Chosen Application: Echo App

#References: In class notes (Weeks 1-7) and labs

#Import Libraries
import sys
from socket import *

#Client Socket Port and Address
server_addr = '192.168.1.73'
svr_port = 12000

#Opening the client socket
cln_socket = socket(AF_INET,SOCK_DGRAM)

#Opening the client socket
message = input('Enter Message: ')
#Client starts sending message to server
cln_socket.sendto(message.encode(),(server_addr, svr_port))

#Client recives a request from the server and prints it out
modifiedMessage, server_addr = cln_socket.recvfrom(1024)
print('Output from Server: ', modifiedMessage.decode())

#Counter for timemout and exception handling
counter = 0

try:
    #Final message from server before disconnection
    print ('Goodbye')
    #Close socket
    cln_socket.close()
    
except timeout:
    #Alert user about timeout
    counter += 1
    print('Timeout')

    #Close the socket
    cln_socket.close()

#Close program
sys.exit(0)
