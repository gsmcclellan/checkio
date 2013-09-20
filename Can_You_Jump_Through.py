"""Greg McClellan
   Created: 8/18/13
   Last Edited: 8/18/13

   Program takes in a list containing an NxN matrix consisting of numbers 0 - 9
   and two tuples at the end representing a starting and ending point. The object
   is to get from start to end going only horizontally or vertically throug zeroes.
   Returns True if this is possible, False otherwise:
"""
def checkio(data):
    matrix, a, b = data
    return do_checkio(matrix, a, b)

def do_checkio(data, a, b, state=set()):

    a, b = tuple(a), tuple(b)

    if b not in state:

        if a not in state:
            state.add(a)

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
    if data[a[0] - 1][a[1]] == 0:
        return True
    else:
        return False

def check_left(data, a):
    if data[a[0] - 1][a[1] - 2] == 0:
        return True
    else:
        return False

def check_up(data, a):
    if data[a[0] - 2][a[1] - 1] == 0:
        return True
    else:
        return False

def check_down(data, a):
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
