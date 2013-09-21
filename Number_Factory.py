""" Number Factory
	Greg McClellan
	Created: 2013-8-26
	Last Edited: 2013-9-20

	Problem:

	Given a positive ( > 0 ) integer N. You should find the smallest 
	positive ( > 0 ) number of X, such that the product of its digits is 
	equal to the number of N. If number X does not exist, then return 0. 
	For one-digit numbers, the answer is a number itself.

	Hints: Remember about prime numbers (or numbers divided at non one 
	digit prime number) and be careful with eternal loops.

	Input: An Integer.

	Output: An Integer.
"""
from itertools import combinations_with_replacement

def checkio(number):
	"""Given 'number', find the smallest integer such that the product of
	its digits is equal to 'number'. If no such integer exists, return 0"""
	factors = one_digit_factors(number)

	if not factors:
		return 0

	# Put a limit to the number of combinations needed
	max_digits = 0
	x = factors[0]
	while x <= number:
		max_digits += 1
		x = x * factors[0]

	for i in range(1, max_digits + 1):
		combinations = list(combinations_with_replacement(factors, i))

		for combination in combinations:
			product = 1

			for digit in combination:
				product = product * digit

			if product == number:
				product_as_int = ''
				
				for digit in combination:
					product_as_int += str(digit)

				return int(product_as_int)

	return 0

def one_digit_factors(number):
	"""Returns a list of one digit factors for given number. If number
	has no one-digit factors (not counting 1), returns false."""
	factors = []
	for i in range(2, 10):
		if number % i == 0:
			factors.append(i)

	return factors

print(checkio(5))