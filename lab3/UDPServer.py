# -*- coding: latin-1 -*-
#	This is a pretend server in the form of a python file.
#
#

from socket import *

serverPort = 12000
# Creates an UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# socket function bind() to assign portNumber to the servers socket
serverSocket.bind(('', serverPort))
print "The server is ready to receive"


# Starts a while loop to allow UDPServer.py to receive packets from clients.
while 1:
	# The received package will be stored in message, and the clients IP and 
	# port number stores in clientAddress.
	# Use recvfrom() function from socket to do this
	message, clientAddress = serverSocket.recvfrom(2048)
	# Changes the message to uppercase
	modifiedMessage = message.upper()
	# Socket function sendto() sends the modifiedMessage to the clientAddress
	serverSocket.sendto(modifiedMessage, clientAddress)