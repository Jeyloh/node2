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


	#modifiedMessage = message.decode('utf-8').upper().encode('utf-8')


	def char_to_bit(character):
		"Brukes for å gjøre message om til bits."
		bit_list = []

		# Hvert element i character refereres til som c
		for c in character:
			# ord() gir oss en integer verdi av hver c
			n = ord(c)
			# Formaterer n som er integer verdier av hver c
			b = "{0:0b}".format(n)
			# Legger til det ferdige resultatet i listen.
			bit_list.append(b)

		print bit_list

		# Denne loopen sjekker hver byte i bit_list og ser om de er større enn 7.
		# Visst de er større enn 7 vet vi at det er unicode, f. eks 'æøå'
		for b in bit_list[:-1]:
			if len(b) > 7:
				if b[0] == "1" and b[1] == "1":
					temp = b + bit_list[bit_list.index(b)+1]
					print temp
					bit_list.insert(bit_list.index(b), temp)
					bit_list.remove(bit_list[bit_list.index(b) + 1])
					bit_list.remove(b)

		print bit_list
		return bit_list

	def to_upper(message):
		dec_list = []

		for c in message:
			c = str(c)

			# Vi formaterer integeren vår med '2' som er binary formatering
			to_dec = int(c, 2) #50085
			# Trekker 32 fra integer for å få uppercase int til lowercasen vår
			upper = to_dec - 32
			# Legger alt til i listen og fjerner hex (u\)
			dec_list.append(("%x" % upper).decode('hex')) # 
		dec_list = ''.join(dec_list)
		return dec_list

	# Bruker begge funksjonene våre på message (sendt fra klient)
	modifiedMessage = to_upper(char_to_bit(message))
	print modifiedMessage

	# Socket function sendto() sends the modifiedMessage to the clientAddress
	serverSocket.sendto(modifiedMessage, clientAddress)







