"""
	Greg McClellan
	Created: 8/26/2013
	Last Edited: 8/26/2013

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

def checkio(a, b, c):
	lengths = [a, b, c]
	perimeter = sum(lengths)

	if perimeter <= 2 * sorted(lengths, reverse = True)[0]:
		return [0, 0, 0]

	angles = [0, 0, 0]

	angles[0] = 180/(1 + b/a + c/a)

	angles[1] = (180 - angles[0])/(1 + c/b)

	angles[2] = 180 - angles[0] - angles[1]

	for i in range(3):
		angles[i] = int(round(angles[i]))

	return sorted(angles)

print(checkio(3, 4, 5))