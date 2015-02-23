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

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = { 	'student1': 'Daniel Eide', \
		'student2': 'Jørgen Lybeck Hansen', \
           	'student3': 'Jørn Utheim-Olsen', \
           	'student3': 'Jonas Dam', \
           	'student3': 'Elaine Sajets', \
           	'student3': 'Christian Fredrik Thorne', \
           	'student3': 'Bastian Strang', \
           	'student3': 'test 8', \
}

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

#
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

def transferBin(string): 
	# vi lager variabel 'l' til en liste av string
	l = list(string)
	# itererer over l for å finne c. 
	for c in l:
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		print "Den binære representasjonen for bokstavene i ordet ditt er %s" % (ascii8Bin(c)) 
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
    for c in l2:
        print "Den heksadesimale representasjonen for bokstavene i ordet ditt er %s" % ascii2Hex(c)
        
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
	uba = []
	# Itererer gjennom det formaterte unicodesumbolet
	for n in range (len(format(character))):
		uba.append("{0:08b}".format(utf8_byte_array[n]))
		# konverterer listen til en string bestående av den binære koden til symbolet
		uni_bin = ' '.join(uba)
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
# Kilder: http://amitsaha.github.io/site/notes/articles/python_linux/article.html

import platform


def printSysInfo():

	print "\nSystem info:"
	print "OS: " +platform.uname()[0]
	print "User Name: " +platform.uname()[1]
	print "Distribution: %s" %(platform.linux_distribution(), )

#   IMPORT PSUTIL OG IMPLEMENTER DEN

printSysInfo()


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('a') == '01100001'
	assert ascii8Bin('A') == '01000001'
	assert transferBin('l') == '6c'
#   assert transferHex('a') == 61
	assert unicodeBin('å') == '11000011 10100101'
	# Dine egne tester
	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()
		

