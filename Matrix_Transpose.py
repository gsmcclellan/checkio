"""Greg McClellan
   Created: 2013-8-12
   Last Edited: 2013-9-20

      2013-9-20: Added main() function

   Program finds the transpose of a given 2D matrix
"""

def checkio(matrix):
    """Function takes the matrix as input and returns it as a transposed 
    matrix"""
    new_matrix = []

    for item in matrix[0]:
        new_matrix.append([])

    for i, item in enumerate(matrix):
        for j, digit in enumerate(item):
            new_matrix[j].append(digit)        

    return new_matrix


def main():

    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

    matrix2 = [[1, 4, 3],
               [8, 2, 6],
               [4, 9, 6],
               [7, 8, 1]]

    matrices = [matrix1, matrix2]

    for matrix in matrices:
      transposed_matrix = checkio(matrix)
      print("\nStarting Matrix: ")

      for line in matrix:
          print("    ", line)

      print("\nTransposed Matrix: ")

      for line in transposed_matrix:
          print("    ", line)


if __name__ == '__main__':
    main()
