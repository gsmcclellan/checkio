"""
	Greg McClellan
	Created: 2013-8-26
	Last Edited: 2013-9-21

		2013-9-21: Reworked the program to use the Law of Cosines

	Problem: 

	You are given the lengths for each side on a triangle. 
	You need to find all three angles for this triangle. 
	If the given side lengths cannot form a triangle 
	(or form a degenerated triangle), then you must return all angles as 0 (zero). 
	The angles should be represented as a list of integers in ascending order. 
	Each angle is measured in degrees and rounded an nearest integer number 
	(Standard mathematical rounding).

	Input: The lengths of the sides of a triangle. Integers.

	Output: Angles of a triangle in degrees. A sorted list of integers.
"""

from math import acos, pi


def checkio(a, b, c):
	lengths = [a, b, c]
	perimeter = sum(lengths)

	if perimeter <= 2 * sorted(lengths, reverse = True)[0]:
		return [0, 0, 0]

	# Law of Cosines:
	# 
	# cos (angle A) = (b**2 + c**2 - a**2)/(2bc)

	angles = [0, 0, 0]

	angles[0] = acos((b**2 + c**2 - a**2)/(2*b*c)) * (180/pi)

	angles[1] = acos((a**2 + c**2 - b**2)/(2*a*c)) * (180/pi)

	angles[2] = acos((a**2 + b**2 - c**2)/(2*a*b)) * (180/pi)

	for i in range(3):
		angles[i] = int(round(angles[i]))

	return sorted(angles)


def main():
	data = []
	data.append([3, 4, 5])

	for item in data:
		print("\nSides: ", item)
		sides = checkio(item[0], item[1], item[2])
		print("Angles", sides)


if __name__ == '__main__':
	main()