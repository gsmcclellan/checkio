"""
	Greg McClellan
	Created: 2013-8-23
	Last Edited: 2013-9-20

		2013-9-20: Added commentation, docstrings

	Program will receive a matrix of ones and zeroes, representing water
	and land respectively. Program will calculate the size of each island
	and return a list of all island sizes.
	Note: Land connected diagonally counts as an island
"""

def checkio(data):
	"""Calculates size of each island and returns as a list"""
	islands = []

	for i in range(len(data)):
		for j in range(len(data[0])):
			x = calculate_land(data, tuple([i, j]))

			if x:
				islands.append(x)

	return sorted(islands)

def calculate_land(data, position, land = 0):
	"""Takes our matrix and a position, returns false if our position is
	 water, else returns the size of the island connected to that point 
	 and turns those land points into water to prevent double counting."""


	if data[position[0]][position[1]] == 1:
		land += 1
		data[position[0]][position[1]] = 0

		if (position[1] < len(data[0]) - 1):
			land = calculate_land(
					data, 
					tuple([position[0], position[1] + 1]), 
					land) # Checks East

		if (position[0] < len(data) - 1) and (position[1] < len(data[0]) - 1):
			land = calculate_land(
					data, 
					tuple([position[0] + 1, position[1] + 1]), 
					land) # Checks Southeast
		
		if (position[0] < len(data) - 1):
			land = calculate_land(
					data, 
					tuple([position[0] + 1, position[1]]), 
					land) # Checks South
		
		if (position[0] < len(data) - 1) and (position[1] > 0):
			land = calculate_land(
					data, 
					tuple([position[0] + 1, position[1] - 1]), 
					land) # Checks Southwest

		if (position[1] > 0):
			land = calculate_land(
					data, 
					tuple([position[0], position[1] - 1]), 
					land) # Checks West
		if (position[0] > 0) and (position[1] > 0):
			land = calculate_land(
					data, 
					tuple([position[0] - 1, position[1] - 1]), 
					land) # Checks Northwest

		if (position[0] > 1):
			land = calculate_land(
					data, 
					tuple([position[0] - 1, position[1]]), 
					land) # Checks North

		if (position[0] > 0) and (position[1] < len(data[0]) - 1):
			land = calculate_land(
					data, 
					tuple([position[0] - 1, position[1] + 1]), 
					land) # Checks Northeast

	return land


def main():
	area1 = [[0, 0, 0, 0, 0],
	    	 [0, 0, 1, 1, 0],
	         [0, 0, 0, 1, 0],
	         [0, 1, 0, 0, 0],
	         [0, 0, 0, 0, 0]]

	area2 = [[0, 0, 0, 0, 0],
	         [0, 0, 1, 1, 0],
	         [0, 0, 0, 1, 0],
	         [0, 1, 1, 0, 0]]

	area3 = [[0, 0, 0, 0, 0, 0],
	         [1, 0, 0, 1, 1, 1],
	         [1, 0, 0, 0, 0, 0],
	         [0, 0, 1, 1, 1, 0],
	         [0, 0, 0, 0, 0, 0],
	         [0, 1, 1, 1, 1, 0],
	         [0, 0, 0, 0, 0, 0]]

	areas = [area1, area2, area3]

	for area in areas:
		print ("Scanning seascape...")
		for line in area:
			print("    ", line)
		print("Islands: ", checkio(area), '\n')


if __name__ == '__main__':
	main()