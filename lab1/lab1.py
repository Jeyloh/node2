# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#         
#
# 	Alle tester og variabler kan flyttes til test. Fullfør dette før mappeinnl.
#		- jørgen
#
#
#

import sys

#   Author:     Jorgen Lybeck Hansen, Elaine Sajets, Daniel Eide, Bastian Strang, Jonas Dam, Christian Thorne
#   Group:      Node 

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '` 


ice = """
       \\/_
  \\,   /( ,/
   \\\\\\' ///
    \\_ /_/
    (./
     '` 
"""

def ascii_bird():
	print ice

ascii_bird()

# 
#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring:
#		6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#		1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#		er 4 desimalt. Antagelse: posisjonsbasert tallsystem og 
#		den mest signifikante bit-en er lengst til venstre
#
#
# Bitwise opererer med tall men behandler dem som om de er string av bits,
# istedenfor single verdier. 
# <<, >>, & (and), | (or), ~ og ^ (exclusive or) er bitwise operators. 
# For å bruke "bitwise and" som oppgaven spør om bruker vi "&" funksjonen. 


def bitAnd(x, y):
	return x&y
print bitAnd(1, 1)

#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
	return x^y
print bitXor(0, 1)

#https://docs.python.org/2/tutorial/datastructures.html
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
# Visst både x og y er 0 blir dette 0. Visst ikke blir dette 1

def bitOr(x, y):
	return x|y
print bitOr(1, 0)

#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110 
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
# 
# ord() funksjonen støtter ikke bruk av f. eks bokstaver som æøå

print "\nSkriv en enkel bokstav. Den kan være stor eller liten:" 
# gjør bokstav valgfri for brukeren
letter = raw_input("> ") 

# definerer en funksjon med letter variabelen
def ascii8Bin(letter): 
	# innhold i funksjonen vår:
	return '{0:08b}'.format(ord(letter)) #formaterer med bruk av ord() funksjonen
# printer resultatet av funksjonen vår
print "Med ord() funksjonen formateres bokstaven din til %r" % (ord(letter))
print "I binær er den %r" % (ascii8Bin(letter))



# 
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#

print "\nSkriv ett ord med max 6 bokstaver, kan være store eller små bokstaver:"
string = raw_input("> ")
#parted = [letter for letter in string]

def transferBin(string): 
	# vi lager variabel 'l' til en liste av string
	l = list(string)
	outstring = ""
	# itererer over l for å finne c.
	i = 0 
	for c in l:
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		print "Den binære representasjonen for '%s' i ordet ditt er %s" % (c, ascii8Bin(c))
		outstring += ascii8Bin(c) + '\n'
		i = i + 1
	return outstring
# bruk funksjonen vår
transferBin(string)



#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#  


print "\nSkriv ett ord med max 6 bokstaver, kan være store eller små bokstaver:"
string = raw_input("> ")

def ascii2Hex(c):
    #innhold i funksjonen vår
    return '{0:02x}'.format(ord(c))
    
def transferHex(string):
    l2 = list(string)
    outstring = ""
    for c in l2:
        print "Den heksadesimale representasjonen for bokstavene i ordet ditt er %s" % ascii2Hex(c)
        outstring += ascii2Hex(c)
    return outstring
        
transferHex(string)

##
## Oppgave 8
## Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
## Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
## Bruker skriver inn en bokstav. Unicode er ok.
#print "\nSkriv en bokstav, gjerne Æ Ø eller Å. Den kan være stor eller liten:" 
#character = unicode(raw_input(), 'utf8')
#
#def unicodeBin(character):
#	# innhold i funksjonen vår:
#	return '{0:08b}'.format(ord(character)) #formaterer med bruk av ord() funksjonen
# printer resultatet av funksjonen vår
#print "Med ord() funksjonen formateres bokstaven din til %r" % (ord(character))
#print "I binær er den %r" % (unicodeBin(character))		

print "\nSkriv en bokstav, gjerne Æ Ø eller Å. Den kan være stor eller liten:" 
char = raw_input("> ")
def unicodeBin(character):
	utf8_byte_array = bytearray(format(character))
	temp = []
	# Itererer gjennom det formaterte unicodesumbolet
	for n in range (len(format(character))):
		temp.append("{0:08b}".format(utf8_byte_array[n]))
		# konverterer listen til en string bestående av den binære koden til symbolet
		uni_bin = ''.join(temp)
	return uni_bin
print unicodeBin(char)

#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#	
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#
#

import psutil
import platform

def sysInfo():

	memory = psutil.virtual_memory().total
	disk = psutil.disk_usage('/').total
	print "OS: " +platform.uname()[0]
	print "Username: " +platform.uname()[1]

	print "\nDatamaskinen din har {0} bits med ram.\n" .format(memory)
	print "Datamaskinen din har en harddisk på {0} bits.\n" .format(disk)
sysInfo() 

"""
Hard drive capacity finnes ved å kjøre kommandoen psutil.disk_usage('/').
Det vil da returneres hvor mye plass man har, hvor mye som er brukt, og prosentandel.

Amount of RAM finnes ved å kjøre kommandoen psutil.virtual_memory(). 
Det vil da returneres hvor mye minne man har i bits, hvor mye som brukes i bits, og prosentandel.

For å gjøre begge disse lettere å lese har vi lagt til .total etter kommandoene. 
Det vil da bare returneres hvor mange bits hver enkelt av de to inneholder.

Dette er dessverre de eneste to man kan finne via psutil, enkelt og greit siden
modulen ikke har støtte for å finne resten. Det er heller ikke mulig å lage en test,
siden returverdiene vil være forskjellig fra maskin til maskin.

For å finne ut de resterende punktene, må man importere modulen platform, som vi har gjort over.
Man kan da finne ut navn på datamaskinen, og hvilket OS den kjører.
"""


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	assert transferBin('Hi') == '01001000\n01101001\n'
	assert transferHex('J') == '4a'
	assert unicodeBin('j') == '01101010'

	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()

#Kilder:

"""
https://pypi.python.org/pypi/psutil
https://code.google.com/p/psutil/wiki/Documentation
https://docs.python.org/2/library/platform.html
http://www.python-course.eu/sys_module.php
https://docs.python.org/3/reference/import.html
http://stackoverflow.com/questions/28266984/python-script-how-to-import-system	
"""

		


