# -*- coding: latin-1 -*-
#	This is a pretend server in the form of a python file.
##
#   Author:     Jorgen Lybeck Hansen, Elaine Sajets, Daniel Eide, Bastian Strang, Jonas Dam, Christian Thorne
#   Group:      Node

"""Oppgaver som mangler: 

4. Sjekk om applikasjonen fungerer for tegn utover ASCII tegnsettet og forklar
hva som skjer. Gjør om applikasjonen slik at den kan overføre hvilke som
helst tegn fra UNICODE karaktersettet. Finnes det en sammenheng mellom
den binære representasjonen for små og store bokstaver også i dette tilfelle?
Forklar.

5. Implementer din egen metode i for overføring fra små til store bokstaver
basert på manipulasjon av den binære representasjonen til tegn. Bruk
rutiner fra LAB1 (operasjoner på bit). Implementer tester for alle rutiner i en
egen funksjon test() ved bruk av assert setninger.

6. Bruk funksjoner fra deres “romerske” modulen for å implementere denne
fuksjonaliteten i en klient-tjener applikasjon. For å få det til, må dere endre
grensesnitt for INNDATA (i klienten). Her kan dere bruke den innebygde
funksjonen i Python raw_input(). Pass på at dere tester for alle eventuelle
feil, som en kommandolinje bruker potensielt kan gjøre.

7. Burde dere bruke TCP protokollen for dere applikasjon i dette tilfelle? Forklar
hvorfor, eventuelt hvorfor ikke
"""

from socket import *

serverPort = 12000
# Creates an UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# socket function bind() to assign portNumber to the servers socket
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

def unicodeBin(character):
	utf8_byte_array = bytearray(format(character))
	temp = []
	# Itererer gjennom det formaterte unicodesumbolet
	for n in range (len(format(character))):
		temp.append("{0:08b}".format(utf8_byte_array[n]))
		# konverterer listen til en string bestående av den binære koden til symbolet
		uni_bin = ''.join(temp)
	return uni_bin

# Starts a while loop to allow UDPServer.py to receive packets from clients.
while 1:
	# The received package will be stored in message, and the clients IP and 
	# port number stores in clientAddress.
	# Use recvfrom() function from socket to do this
	message, clientAddress = serverSocket.recvfrom(2048)
	# Decodes message to utf8, change it to uppercase and then encode it back to be sent again


#	modifiedMessage = message.decode('utf-8').upper().encode('utf-8')

	# ex. message = ""
	# Our message is stored as a number of bits in variable modifiedMessage
	modifiedMessage = unicodeBin(message) 

	print modifiedMessage

	#int formatting, 
	modifiedMessage = '%x' %int(message, 2).decode('hex')
	

	# Socket function sendto() sends the modifiedMessage to the clientAddress
	serverSocket.sendto(modifiedMessage, clientAddress)





def unicode_bytearray():
	"""Here we want to do what we did in line 49 while using a function with bytearray."""
	pass


"""
Linje 24 skal gjøres manuelt med bruk av bitwise operators. Vi bruker '^32' (xOr) for å
finne 32 bit plassen i byten vår. Dette switcher den fra 0 > 1 eller fra 1 > 0, noe som betyr
at verdien av bittene vil bli stor/liten bokstav.

a = 1100001 = 97
A = 1000001 = 65

bruk bin() funksjon for å gjøre de om til bits 
Skriv en kode som flipper 32 bit plassen fra 0 til 1 (bruk 65^32)

message = # input fra client

binary_message = bin(message)
binary_message * 65^32 # flipper 65 som er 'a' til å bli 97 som er 'A'

test = 65^32
bin(test)
"""

"""
Tests from terminal:

>>> print "example"
example
>>> print "exámple"
exámple
>>> print "exámple".upper()
EXáMPLE
>>> print u"exámple".upper()
EXÁMPLE

"""