"""
	Greg McClellan
	Created: 8/23/2013
	Last Edited: 8/23/13

	Program will receive a matrix of ones and zeroes, representing water and land respectively.
	Program will calculate the size of each island and return a list of all island sizes.
"""

def checkio(data):
	islands = []

	for i in range(len(data)):
		for j in range(len(data[0])):
			x = calculate_land(data, tuple([i, j]))

			if x:
				islands.append(x)

	return sorted(islands)

def calculate_land(data, position, land = 0):

	#Takes our matrix and a position, returns false if our position is water, else returns the size of
	#the island connected to that point and turns those land points into water to prevent double counting.


	if data[position[0]][position[1]] == 1:
		land += 1
		data[position[0]][position[1]] = 0

		if (position[1] < len(data[0]) - 1):
			land = calculate_land(data, tuple([position[0], position[1] + 1]), land) #Checks to the right

		if (position[0] < len(data) - 1) and (position[1] < len(data[0]) - 1):
			land = calculate_land(data, tuple([position[0] + 1, position[1] + 1]), land) #checks diagonally down and right
		
		if (position[0] < len(data) - 1):
			land = calculate_land(data, tuple([position[0] + 1, position[1]]), land) #checks down
		
		if (position[0] < len(data) - 1) and (position[1] > 0):
			land = calculate_land(data, tuple([position[0] + 1, position[1] - 1]), land) #checks diagonally down and left

		if (position[1] > 0):
			land = calculate_land(data, tuple([position[0], position[1] - 1]), land) #checks to the left

		if (position[0] > 0) and (position[1] > 0):
			land = calculate_land(data, tuple([position[0] - 1, position[1] - 1]), land) #Checks up and left

		if (position[0] > 1):
			land = calculate_land(data, tuple([position[0] - 1, position[1]]), land) #checks up

		if (position[0] > 0) and (position[1] < len(data[0]) - 1):
			land = calculate_land(data, tuple([position[0] - 1, position[1] + 1]), land)

	return land

input1 = [[0, 0, 0, 0, 0],
    	  [0, 0, 1, 1, 0],
          [0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0]]

input2 = [[0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 1, 0],
          [0, 1, 1, 0, 0]]

input3 = [[0, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 1],
          [1, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0]]


print(checkio(input3))