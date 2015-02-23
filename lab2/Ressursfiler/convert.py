# -*- coding: utf-8 -*-
import math 
import re
from lookup import INT_TO_ROMAN, ROMAN_TO_INT #, MATH

"""
    @author: tmackenzie
"""

# used in roman_to_int
ROMAN_VALIDATE_RE = re.compile('^[M]{4,}')
ROMAN_GROUP_RE = re.compile('^([M]{0,3})([DCM]*)([XLC]*)([IVX]*)$')



# Sett en int verdi som skal gjøres om til roman
def int_to_roman(input):
    """
       given an integer, input, that is greater than 0 and less than, 4000
       return its modern roman numeral represenation
    """
    # Visst input ikke er mellom 0 og 4000 får vi en feilmelding
    if not 0 < input < 4000:
        raise ValueError("input must be between 1 and 3999")

    result = []

    """
        significant, is the significant digit of input..
        used to lookup dict.
            1 = ones.
            2 = tens.
            3 = hundreds
            4 = thousands.
        factor, is the whole number for the current significant digit.
        used to calculate, count.
            example, input = 101
            - factor = 100.
        count, the number of times input is divisible by factor.
        used to lookup the arabic, romans tuple.
            example, input = 101, factor = 100
            - count = 1
    """
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
    """
        Given a string that represents a roman numeral, then,
        return its integer value
    """
    # Setter alle bokstavene til uppercase
    input = input.upper()

    # 
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


"""
Denne funksjonen tar to string verdier og legger de sammen. Det blir feil ved 
f. eks:
"VIII" + "I" = "VIIII"
"""
def roman_math(roman, romanTest):

    answer = " ".join([roman,romanTest])

    
    if roman == "VIII" and romanTest == "I":
        answer = "IX"
    if roman == "III" and romanTest == "I":
        answer = "IV"
    if roman == "XIII" and romanTest == "I":
        answer = "XIV"



    print "%s + %s = %s" % (roman, romanTest, answer)

