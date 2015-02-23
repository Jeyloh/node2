#  # -*- coding: utf-8 -*- 
#
# Oppgave
# Designe en module i Python som kan overføre fra det desimale til det romerske
# tallsystemet og omvendt.
# Implementere addisjon av to romerske tall (uten å bruke overgangen til
# desimaltall).
# For å få ekstra poeng, implementer også subtraksjon og multiplikasjon.
# Innlevering skal inneholde en module is105roman.py og en egen fil hvor man
# demonstrerer hvordan funksjoner i modulen fungerer (testing). 
#
# Janis' ressurs: http://turner.faculty.swau.edu/mathematics/materialslibrary/roman/
# Løsningsforslag: http://code.activestate.com/recipes/415384-decimal-to-roman-numerals/
#
#   Liste / oversikt over definisjon av romertallene
#   I er 1, V er 5, osv
#
#   Konvertere alle romertallene til tall (desimanl, 1, 5, 100 ..)
#   liste inneholder elementer [element1, element2, element3, ...]
#   ex: element1 er X=10
#
#   konvertere hver enkel bokstav til tallverdien
#   hvordan de er plassert i forhold til verdi for 
#   aa legge sammen eller trekke fra
#
#   To lister, et med desimalt og et med romersk ???
#   MODUL: roman_number, roman, roman_converter 
#   FUNSKJON 1: convert, to_roman, int_to_roman, decimal_to_roman
#       OUTPUT: romertall
#       INPUT: desimaltall
#       IMPLEMENTASJON: 
#   FUNSKJON 2: roman_to_int, roman_to_decimal
#   FUNSKJON 3: subtraction, roman_subtraction,
#   FUNKSJON 4: addition, ..
#
#   import roman_converter as htrc // htrc representerer her modul
#   htrc.subtraction 
#   htrc.int_to_roman(int, [decimal, num
#
#   "I" 1
#   "V" 5
#   "IIII" 4
#   "IIVII" addisjon før substraksjon!!
#   "IV" 4

#   Posisjonsbasert vs posisjonsbasert
#
#   Forutsetning -> hvis noe => feil
#   
#   Funskjon som henter INPUT-en
#   Må kunne liste ut alle funskjonene i en modul 
#   (representere verdiene til romertallene)
#
#   TESTING AV INPUT
#   Sjekke om INPUT fungerer (er tegn korrekte, er de tall)   
#   Hvis man har romertall som ikke er direkte representeres, gi feilmelding
#   1-4999
#
#   Jo flere betingelser, jo mindre konsistent (dårligere?)

def int_to_roman(int):
    """
        Converts a decimanl number to roman number.
        Example: int_to_roman(10) => "x"
    """
    
    return "x"
    pass

def roman_to_int(roman):
    pass
    
print int_to_roman.__doc__
print int_to_roman(10)