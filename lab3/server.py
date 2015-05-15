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


# Starts a while loop to allow UDPServer.py to receive packets from clients.
while 1:
	# The received package will be stored in message, and the clients IP and 
	# port number stores in clientAddress.
	# Use recvfrom() function from socket to do this
	message, clientAddress = serverSocket.recvfrom(2048)
	# Decodes message to utf8, change it to uppercase and then encode it back to be sent again


	#modifiedMessage = message.decode('utf-8').upper().encode('utf-8')

	def char_to_bit(character):
		
		output = []

		for c in character:
			n = ord(c)
			b = "{0:0b}".format(n)
			output.append(b)

		print output
		for b in output[:-1]:
			if len(b) > 7:
				if b[0] == "1" and b[1] == "1":
					temp = b + output[output.index(b)+1]
					print temp
					output.insert(output.index(b), temp)
					output.remove(output[output.index(b) + 1])
					output.remove(b)

		print output
		return output

	def to_upper(message):
		
		output = []

		for c in message:
			c = str(c)

			to_dec = int(c, 2) #50085
			upper = to_dec - 32

			output.append(("%x" % upper).decode('hex'))
		output = ''.join(output)
		return output

	modifiedMessage = to_upper(char_to_bit(message))



	print modifiedMessage

	

	# Socket function sendto() sends the modifiedMessage to the clientAddress
	serverSocket.sendto(modifiedMessage, clientAddress)


def test():
	pass


