import sys

mapping = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


"""
def arab_to_roman( number ):
   if number <= 0: return ''

   ret = ''
   for arab, roman in mapping:
       while number >= arab:
           ret += roman
           number -= arab

   return ret
"""
def roman_to_arab(txt):
    txt = txt.upper()
    ret = 0
    
    try:
	    for arab, roman in mapping:
	        while txt.startswith(roman):
	            ret += arab
	            txt = txt[len( roman ):]
		
		return ret
	except:
		return "BadRomanNumeral"
	else:
	   if number <= 0: return ''

	   ret = ''
	   for arab, roman in mapping:
	       while number >= arab:
	           ret += roman
	           number -= arab

	   return ret


print arab_to_roman(29)
print roman_to_arab('XXKK')

def roman_int(string):
	mapping = {'I': 1,'V': 5, 'X': 10, 'XL': 40, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	doubles = {'IV': 4,'IX': 9, 'CM':900, 'CD':400}
	summ = 0
	try:
		if int(1):
			summ = sum(map(lambda x: mapping[x], string))
			if (string.find('IV') or string.find('IX')):
				summ = summ - 2
			elif  (string.find('CM') or string.find('CD')):
				summ = summ - 200
			return summ

	except ValueError:
		return 'BadRomanNumeral'


print roman_int('XXIX')
print roman_int('LXXVIII')
print roman_int('CM')

singles = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

doubles = {
    ('I', 'V'): 3,
    ('I', 'X'): 8,
    ('X', 'L'): 30,
    ('X', 'C'): 80,
    ('C', 'D'): 300,
    ('C', 'M'): 800,
}

def roman_to_arabic(val):
    if str(val):
	    number = 0
	    prev_literal = None
	    for literal in val:
	        if prev_literal and singles[prev_literal] < singles[literal]:
	            number += doubles[(prev_literal, literal)]
	        else:
	            number += singles[literal]
	        prev_literal = literal
	    return number


print roman_to_arabic('XXIX')
print roman_to_arabic('LXXVIII')
print roman_to_arabic('CM')
