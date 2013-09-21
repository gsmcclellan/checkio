"""Greg McClellan
   Created: 2013-8-18
   Last Edited: 2013-9-20

      2013-9-20: Added commentation, docstrings.
                 Replaced default value of do_checkio() from set() to
                 None with a check to initialize the set at the start of
                 the function to avoid having a mutable default value.

   Program takes in a list containing an NxN matrix consisting of numbers 0 - 9
   and two tuples at the end representing a starting and ending point. The object
   is to get from start to end going only horizontally or vertically throug zeroes.
   Returns True if this is possible, False otherwise:
"""
def checkio(data):
    """Takes data as given by CheckIO website, and parses it into data
    described by the CheckIO problem page, then calls do_checkio()"""
    matrix, a, b = data
    return do_checkio(matrix, a, b)

def do_checkio(data, a, b, state=None):
    """Checks a 2D matrix to see if there is a continuous path from
    A to B consisting of zeroes"""

    # if no input for state given, create empty set
    if not state:
      state = set()

    a, b = tuple(a), tuple(b)

    if b not in state:

        if a not in state:
            state.add(a)

            # For each position, check all values to right, left, up, 
            # and down, then call function recursively
            if a[1] < len(data):
                if check_right(data, a):
                    r = do_checkio(data, [a[0], a[1] + 1], [b[0], b[1]], state)
                    if r:
                      return r

            if a[0] < len(data):
                if check_down(data, a):
                    r = do_checkio(data, [a[0] + 1, a[1]], [b[0], b[1]], state)
                    if r:
                      return r

            if a[1] > 1:
                if check_left(data, a):
                    r = do_checkio(data, [a[0], a[1] - 1], [b[0], b[1]], state)
                    if r:
                      return r

            if a[0] > 1:
                if check_up(data, a):
                    r = do_checkio(data, [a[0] - 1, a[1]], [b[0], b[1]], state)
                    if r:
                      return r

                

    return (b in state)

def check_right(data, a):
    """Checks value to the right of position for a 0"""
    if data[a[0] - 1][a[1]] == 0:
        return True
    else:
        return False

def check_left(data, a):
    """Checks value to the left of position for a 0"""
    if data[a[0] - 1][a[1] - 2] == 0:
        return True
    else:
        return False

def check_up(data, a):
    """Checks value above position for a 0"""
    if data[a[0] - 2][a[1] - 1] == 0:
        return True
    else:
        return False

def check_down(data, a):
    """Cheks value below position for a 0"""
    if data[a[0]][a[1] - 1] == 0:
        return True
    else:
        return False


data1 = [[[0, 0, 5, 4, 0],
          [0, 1, 5, 0, 0],
          [0, 0, 0, 7, 2],
          [8, 0, 0, 0, 0],
          [0, 9, 0, 1, 0]], [1, 1], [5, 3]] #True

data2 = [[[0, 0, 5, 4, 0],
          [0, 0, 5, 0, 0],
          [0, 0, 0, 7, 2],
          [8, 0, 0, 4, 0],
          [0, 9, 0, 1, 0]], [1,1], [1,5]] #False

data3 = [[[0,0,5,4,0],
          [0,0,5,0,0],
          [0,0,0,7,2],
          [8,0,0,4,0],
          [0,9,0,1,0]],[1,1],[5,5]] #False




print (checkio(data3))
