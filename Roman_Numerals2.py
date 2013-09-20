"""
	This is a more efficicient method of solving Roman_Numerals.py.
	I did not write this algorithm, but I copied it down for the purposes 
	of learning and remembering the principles behind it.
"""

def roman_numerals(number):
	roman_numeral = ''
	roman_mappings = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
					  40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 
					  400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

	for intVal in sorted(roman_mappings.keys(), reverse = True):
		while number >= intVal:
			roman_numeral += roman_mappings[intVal]
			number -= intVal


	return roman_numeral

for i in range(1, 4001):
	print(i, ": ", roman_numerals(i))