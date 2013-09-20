"""Greg McClellan
   Created: 8/10/13
   Last Edited 8/10/13

   Program will find one of possible routes through a 2d maze given as a matrix of ones and zeroes
"""

INITIAL_POSITION = [1, 1]
ENDING_POSITION = [10, 10]

class Position(object):
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%i, %i)" %(self.x, self.y)

    def move_right(self):
        self.x += 1
        return 'E'
        
    def move_left(self):
        self.x -= 1
        return 'W'

    def move_up(self):
        self.y -= 1
        return 'N'

    def move_down(self):
        self.y += 1
        return 'S'

    def move(self, labyrinth, route):
        if self.poss_moves(labyrinth, route) < 1:
            return False
        if labyrinth[self.y][self.x + 1] == 0 and route[len(route) - 1] != 'W':
            return self.move_right()
        elif labyrinth[self.y + 1][self.x] == 0 and route[len(route) - 1] != 'N':
            return self.move_down()
        elif labyrinth[self.y - 1][self.x] == 0 and route[len(route) - 1] != 'S':
            return self.move_up()
        elif labyrinth[self.y][self.x - 1] == 0 and route[len(route) - 1] != 'E':
            return self.move_left()
        else:
            return False

    def poss_moves(self, labyrinth, route):
        count = 0
        if labyrinth[self.y][self.x + 1] == 0 and route[len(route) - 1] != 'W':
            count += 1
        elif labyrinth[self.y + 1][self.x] == 0 and route[len(route) - 1] != 'N':
            count += 1
        elif labyrinth[self.y - 1][self.x] == 0 and route[len(route) - 1] != 'S':
            count += 1
        elif labyrinth[self.y][self.x - 1] == 0 and route[len(route) - 1] != 'E':
            count += 1

        return count
        
    def back_track(self, labyrinth, route):
        while self.poss_moves(labyrinth, route) < 1:
            if route[len(route) - 1] == 'E':
                labyrinth[self.y][self.x] = 1
                self.move_left()
                route.pop()
            elif route[len(route) - 1] == 'S':
                labyrinth[self.y][self.x] = 1
                self.move_up()
                route.pop()
            elif route[len(route) - 1] == 'N':
                labyrinth[self.y][self.x] = 1
                self.move_down()
                route.pop()
            else:
                labyrinth[self.y][self.x] = 1
                self.move_right()
                route.pop()

def checkio(labyrinth):
    position = Position(INITIAL_POSITION[0], INITIAL_POSITION[1])
    goal = Position(ENDING_POSITION[0], ENDING_POSITION[1])
    route = [0]

    while position != goal:
        print(route)
        if position.poss_moves(labyrinth, route) > 0:
            if position.x == goal.x and position.y == goal.y:
                break
            route += position.move(labyrinth, route)
        else:
            position.back_track(labyrinth, route)

    route.remove(0)

    return "".join(route)


labyrinth1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

labyrinth2 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

labyrinth3 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

labyrinth4 = [[1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,1,0,0,0,1,0,0,0,0,1],
              [1,0,1,0,1,0,1,0,1,1,0,1],
              [1,0,1,0,1,0,1,0,1,0,0,1],
              [1,0,1,0,1,0,1,0,1,0,1,1],
              [1,0,1,0,1,0,1,0,1,0,0,1],
              [1,0,1,0,1,0,1,0,1,1,0,1],
              [1,0,1,0,1,0,1,0,1,0,0,1],
              [1,0,1,0,1,0,1,0,1,0,1,1],
              [1,0,1,0,1,0,1,0,1,0,0,1],
              [1,0,0,0,1,0,0,0,1,1,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1]]

print(checkio(labyrinth4))
    
