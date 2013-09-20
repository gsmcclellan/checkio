from itertools import combinations

def checkio(data):
	x = combinations(data, 3)

	print(x)

	return 0

data1 = [4, 2, 10]
data2 = [1, 2, 3]
data3 = [5, 2, 9, 6]

print(combinations(data3, 3))