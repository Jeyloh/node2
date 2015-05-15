def char_to_bit(character):
	utf8_byte_array = bytearray(format(character))
	temp = []
	# Itererer gjennom det formaterte unicodesumbolet
	for n in range (len(format(character))):
		temp.append("{0:08b}".format(utf8_byte_array[n]))
		# konverterer listen til en string bestående av den binære koden til symbolet
		uni_bin = ''.join(temp)
	return uni_bi



def 


message = "å"
new_bin = char_to_bit(message) #1100001110100101
to_dec = int(char_to_bit, 2) #50085
upper = to_dec - 32

result = ("%x" % upper).decode('hex')

return result



	#int formatting, 
	modifiedMessage =' %x' %int("1100001110100101", 2).decode('hex')



	# ex. message = ""
	# Our message is stored as a number of bits in variable modifiedMessage


modifiedMessage = char_to_bit(message) 


^32 






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