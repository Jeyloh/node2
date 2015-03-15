# -*- coding: latin-1 -*-
#	This is a pretend server in the form of a python file.
##
#   Author:     Jorgen Lybeck Hansen, Elaine Sajets, Daniel Eide, Bastian Strang, Jonas Dam, Christian Thorne
#   Group:      Node

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
	# Decodes message to utf8, change it to uppercase and then encode it back to be sent again
	modifiedMessage = message.decode('utf-8').upper().encode('utf-8')
	# Socket function sendto() sends the modifiedMessage to the clientAddress
	serverSocket.sendto(modifiedMessage, clientAddress)



def unicode_bytearray():
	"""Here we want to do what we did in line 24 while using a function with bytearray."""
	pass



print "Skriv en bokstav, gjerne Æ Ø eller Å. Den kan være stor eller liten:" 
char = raw_input("> ")
def unicodeBin(character):
	utf8_byte_array = bytearray(format(character))
	uba = []
	# Itererer gjennom det formaterte unicodesumbolet
	for n in range (len(format(character))):
		uba.append("{0:08b}".format(utf8_byte_array[n]))
		# konverterer listen til en string bestående av den binære koden til symbolet
		uni_bin = ' '.join(uba)
	return uni_bin
print unicodeBin(char)


"""
Linje 24 skal gjøres manuelt med bruk av bitwise operators. Vi bruker '^32' (xOr) for å
finne 32 bit plassen i byten vår. Dette switcher den fra 0 > 1 eller fra 1 > 0, noe som betyr
at verdien av bittene vil bli stor/liten bokstav."""

a = 1100001 = 97
A = 1000001 = 65

bruk bin() funksjon for å gjøre de om til bits 
Skriv en kode som flipper 32 bit plassen fra 0 til 1 (bruk 65^32)

message = # input fra client

binary_message = bin(message)
binary_message * 65^32 # flipper 65 som er 'a' til å bli 97 som er 'A'

test = 65^32
bin(test)
