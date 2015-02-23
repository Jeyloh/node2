# -*- coding: latin-1 -*-
#	This is a pretend client in the form of a python file.
#
#

# Import the socket module and all it's contents. The socket module is used
# a lot in network communiation with python
from socket import *

# Sets the serverName. A DNS lookup will be performed and fetch the IP address.
serverName = 'localhost'
# Sets the serverPort to 12 000
serverPort = 12000

# Creates the clientSocket by using functions from the socket module
#	Param1: Indicates the address family
#	Param2: The soket is of type SOCK_DGRAM which means it's a UDP socket
# We don't specify port number yet, instead we let the OS do this for us.
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Create a message to be sent from the UDP socket
message = raw_input('Input lowercase sentence:')


# We use our clientSocket (that is a variable for socket module) and call the
# sendto() function from socket to send the message. As params we use the
# message to send, serverName and serverPort
clientSocket.sendto(message.encode("utf8"),(serverName, serverPort))

# When we receive a packet the message is stored in modifiedMessage and
# the packets source address is stored in serverAddress. 
# ServerAddress contains both the servers IP and the port number.
# We use recvfrom() function of socket and give it the buffer size 2048
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# Simply prints out message after 
print modifiedMessage
# Shut down our socket to terminate the process
clientSocket.close()