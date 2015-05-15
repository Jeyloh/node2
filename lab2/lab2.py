# -*- coding: utf-8 -*-
#
#   Author:     Jorgen Lybeck Hansen, Elaine Sajets, Daniel Eide, Bastian Strang, Jonas Dam, Christian Thorne
#   Group:      Node
#	
#	Ressurser: 
#	https://docs.python.org/2/tutorial/datastructures.html +\
#	http://turner.faculty.swau.edu/mathematics/materialslibrary/roman/
#	https://github.com/tmackenzie/roman/blob/master/roman/convert.py 
#
#	Testet i Python versjon 2.7.6

import re
import math
from lab2_dict import INT_TO_ROMAN, ROMAN_TO_INT

# used in roman_to_int
ROMAN_VALIDATE_RE = re.compile('^[M]{4,}')
ROMAN_GROUP_RE = re.compile('^([M]{0,3})([DCM]*)([XLC]*)([IVX]*)$')



# Sett en int verdi som skal gjøres om til roman
def int_to_roman(input):

    # Visst input ikke er mellom 0 og 4000 får vi en feilmelding
    if not 0 < input < 4000:
        raise ValueError("input must be between 1 and 3999")

    result = []

    # Forklaring på math.log10(x):
    # Log base 10, also known as the common logarithm or decadic logarithm, is the logarithm 
    # to the base 10. The common logarithm of x is the power to which the number 10 must be 
    # raised to obtain the value x. For example, the common logarithm of 10 is 1, the common 
    # logarithm of 100 is 2 and the common logarithm of 1000 is 3. It is often used in various 
    # engineering fields, logarithm tables and handheld calculators.
    #   - 0-9 = 0,x. 10-99 = 1,x. 100-999 = 2,x. 1000-9999 = 3,x.
    #
    # Så lenge input ikke er 0 (si at vi har skrevet inn 15)
    while input != 0:

        # Variabel som tar int(math.log10(15)) = 1.176 + 1 = 2.176. I lookup.INT_TO_ROMAN dictionary
        # finner den et tall i '2' lista. Dette er gjort pga hastighet.
        significant = int(math.log10(input)) + 1

        # Variabel = 10 ** (2.176 - 1) = 
        # factor = 10 ** 1.176 (Visst vi tastet inn 15 i input)
        # Exponent - Performs exponential (power) calculation on operators  
        # a**b will give 10 to the power 20
        factor = 10 ** (significant - 1)

        # Variabel som tar 15 / 1.176 
        count = (input / factor)

        # Henter de romerske tallene
        number, roman = INT_TO_ROMAN[significant][count]
        result.append(roman)

        # this could just be, count * factor, its not b/c of speed.
        input -= number

    return ''.join(result)


def roman_to_int(input):

    # Setter alle bokstavene til uppercase
    input = input.upper()


    
    if ROMAN_VALIDATE_RE.match(input) or input == "NULLA":
        raise ValueError("input must be between I and MMMCMXCIX")

    parsed_input = ROMAN_GROUP_RE.match(input)

    if parsed_input is None:
        raise ValueError("Input must be a Roman Numeral")

    result = 0
    for roman_numeral in parsed_input.groups():
        try:
            result += ROMAN_TO_INT[roman_numeral]
        except KeyError:
            pass

    return result


def addition(roman1, roman2):

    # Replace subtractives
    substitution = {    "IV": "IIII",
                        "IX": "VIIII",
                        "XL": "XXXX",
                        "XC": "LXXXX",
                        "CD": "CCCC",
                        "CM": "DCCCC"
    }

    # Go through substitution and replace key with value for roman1 and roman2
    for key, value in substitution.iteritems():
        if roman1 == key:
            roman1 = value
        elif roman2 == key:
            roman2 = value

    # Variable temp joins roman1 and roman2 after replacing substitutes. "IXIII"
    temp = "".join([roman1, roman2])


    # Create a list to append 
    roman_result = []

    # A string where we can find each roman letter
    roman_letters = "MDCLXVI"
    # If our string roman_letters 
    for char in roman_letters:
        # and our string temp 
        for item in temp:
            # contains the same value
            if item == char:
                # append that item
                roman_result.append(item)
 
    # https://docs.python.org/2/tutorial/datastructures.html  <- 5.1.4 List Comprehension

    # We take our roman_result list with the appended items and joins them to a string
    # Then we call our own revert() function on this string to give us the answer.
    return(revert("".join(roman_result)))


def revert(rom_num):

    # Create a list with necessary replacements to do additions.
    replace_list = {
                    "IIIII": "V",
                    "IIII": "IV",
                    "VIIIII": "X",
                    "VIIII": "IX",
                    "VV": "X",
                    "XXXXX": "L",
                    "XXXX": "XL",
                    "LXXXXX": "C",
                    "LXXXX": "XC",
                    "LL": "C",
                    "CCCCC": "D",
                    "CCCC": "CD",
                    "DCCCCC": "M",
                    "DCCCC": "CM",
                    "DD": "M",
    }

    # for keys and values in replace_list
    for key, value in replace_list.iteritems():
        # change key with values in rom_num 
        rom_num = rom_num.replace(key, value)

    return rom_num


def subtraction(rom1, rom2):
    temp1 = roman_to_int(rom1) 
    temp2 = roman_to_int(rom2)

    temp3 = temp1 - temp2

    return int_to_roman(temp3)


def test():
    assert roman_to_int("MDCCLXVI") == 1706
    assert int_to_roman(3910) == "MMMCMX"
    assert addition("XVI", "MCIIII") == "MCXX"

    print "Test passed!"

test()
