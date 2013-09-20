"""
	Greg McClellan
	Created: 8/25/2013
	Last Edited: 8/25/2013

	Problem:

	Roman numerals come from the ancient Roman numbering system. 
	They are based on specific letters of the alphabet which are 
	combined to signify the sum (or, in some cases, the difference) 
	of their values. The first ten Roman numerals are:

	I, II, III, IV, V, VI, VII, VIII, IX, and X.

	The Roman numeral system is decimal based but not directly positional 
	and does not include a zero. Roman numerals are based on combinations 
	of these seven symbols:

	Symbol Value

	I 1 (unus)
	V 5 (quinque)
	X 10 (decem)
	L 50 (quinquaginta)
	C 100 (centum)
	D 500 (quingenti)
	M 1,000 (mille)

	More additional information about roman numerals can be found on the 
	Wikipedia article.

	For this task, you should return a roman numeral using the specified 
	integer value ranging from 1 to 3999.

	Input: An integer ranging from 1 to 3999.

	Output: A string in the form of a Roman numeral.
"""

def roman_numerals(number):
	if number < 4:
		return 'I'*number

	elif number == 4:
		return 'IV'

	elif number < 9:
		return 'V' + roman_numerals(number % 5)

	elif number == 9:
		return 'IX'

	elif number < 40:
		return ('X' * int(number/10)) + roman_numerals(number % 10)

	elif number < 50:
		return 'XL' + roman_numerals(number % 40)

	elif number < 90:
		return 'L' + roman_numerals(number % 50)

	elif number < 100:
		return 'XC' + roman_numerals(number % 90)

	elif number < 400:
		return ('C' * int(number/100)) + roman_numerals(number % 100)

	elif number < 500:
		return 'CD' + roman_numerals(number % 400)

	elif number < 900:
		return 'D' + roman_numerals(number % 500)

	elif number < 1000:
		return 'CM' + roman_numerals(number % 900)

	else:
		return ('M' * int(number/1000)) + roman_numerals(number % 1000)

for i in range(1, 4001):
	print(i, ": ", roman_numerals(i))