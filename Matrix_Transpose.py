"""Greg McClellan
   Created: 8/12/13
   Last Edited: 8/12/13

   Program finds the transpose of a given 2D matrix
"""

def checkio(matrix):
    #Function takes the matrix as input and returns it as a transposed matrix
    new_matrix = []

    for item in matrix[0]:
        new_matrix.append([])
    for i, item in enumerate(matrix):
        for j, digit in enumerate(item):
            new_matrix[j].append(digit)        

    return new_matrix

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[1, 4, 3],
           [8, 2, 6],
           [4, 9, 6],
           [7, 8, 1]]

print(checkio(matrix2))
