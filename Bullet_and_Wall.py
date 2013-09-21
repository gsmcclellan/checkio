""" Bullet and Wall
    Greg McClellan
    Date Created: unk
    Last Edited: 2013-9-20

        2013-9-20: Added commentation and docstrings
""" 

class Coordinate(object):
    """Class containing an x and y coordinate"""
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    def __repr__(self):
        return "(%.2f, %.2f)" %(self.x, self.y)

class Line(object):
    """Line class consisiting of slope and y-intercept"""
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def __repr__(self):
        return "y = %.2fx + %.2f" %(self.m, self.b)

    def intersect(self, other_line):
        """checks if self and another line intersect"""

        # If other line is vertical, call same function with inputs 
        # swapped to handle non-slope
        if type(other_line) == VerticalLine:
            return other_line.intersect(self)

        # If lines are parallel
        if self.m == other_line.m:
            # If lines are identical
            if self.b == other_line.b:
                return Coordinate([self.b, 0])
            # Lines don't intersect
            else:
                return False

        # Common case - use substitution to calculate intersect
        else:
            x = round((other_line.b - self.b)/(self.m - other_line.m), 4)
            y = round((self.m * x + self.b), 4)
            return Coordinate([x, y])

class VerticalLine(Line):
    """Vertical line class consisting only of x intercept"""
    def __init__(self, x_inter):
        self.x_inter = x_inter

    def __repr__(self):
        return "Vertical line intersects x-axis at %s" %(self.x_inter)

    def intersect(self, other_line):
        y = other_line.m*self.x_inter + other_line.b
        return Coordinate([self.x_inter, y])

def create_line(coord1, coord2):
    """Returns a line passing through 2 coordinates"""

    # If line is vertical
    if coord1.x == coord2.x:
        return VerticalLine(coord1.x)

    # Otherwise calculate line
    else:
        m = (coord1.y - coord2.y)/(coord1.x - coord2.x)
        b = coord1.y - m * coord1.x
        return Line(m, b)

    


def bullet_and_wall(list_of_coords):
    """Given 4 coordinates, find whether the bullet intersects the wall.
    The first two coordinates represent the two endpoints of our wall
    The last two coordinates represent the starting poing of the bullet
    and a second point the bullet passes through"""

    # Create variables for inputs
    w1, w2 = Coordinate(list_of_coords[0]), Coordinate(list_of_coords[1])
    a, b = Coordinate(list_of_coords[2]), Coordinate(list_of_coords[3])

    # generate lines for wall and bullet (bullet is actually a ray,
    # and wall is actually a line segment - checks for that later)
    wall_line = create_line(w1, w2)
    bullet_line = create_line(a, b)

    # First check: Find where the two lines intersect
    intersect = wall_line.intersect(bullet_line)

    # Vertical wall
    if w1.x == w2.x:
        # If bullet is traveling east, but wall is to the west
        if b.x >= a.x and w1.x < a.x and w2.x < a.x:
            return False
        # If bullet is traveling west, but wall is to the east
        elif b.x <= a.x and w1.x > a.x and w2.x > a.x:
            return False
            
    # If intersect exists
    if intersect:
        # If intersect is North of actual wall
        if intersect.y > w1.y and intersect.y > w2.y:
            return 
        # If intersect is South of actual wall
        elif intersect.y < w1.y and intersect.y < w2.y:
            return False
        # If intersect is East of actual wall
        elif intersect.x > w1.x and intersect.x > w2.x:
            return False
        # If intersect is West of actual wall
        elif intersect.x < w1.x and intersect.x < w2.x:
            return False

        # If bullet is moving East
        if b.x > a.x:
            # If intersect is West of starting point
            if a.x > intersect.x:
                return False
        # Bullet moving west
        elif b.x < a.x:
            # Intersect is East of start
            if a.x < intersect.x:
                return False
        # Bullet is traveling due North or due South
        else:
            # North
            if b.y > a.y:
                # Intersect is South of start
                if a.y > intersect.y:
                    return False
            # South
            elif b.y < a.y:
                # Intersect is North of start
                if a.y < intersect.y:
                    return False

        # After passing all checks, return True
        return True

    # If no intersection, return False
    else:
        return False

    

coord = Coordinate([1, 2])
line = Line(2, 1)
line2 = Line(.5, 2)
intersection = line.intersect(line2)
#wall = create_wall(Coordinate([0, 0]), Coordinate([0, 2]))

coord1 = Coordinate([0, 0])
coord2 = Coordinate([0, 2])
#wall = VerticalLineSegment(create_line(coord1, coord2), coord1, coord2)


def main():
    list_of_coords = []
    list_of_coords.append([[0, 0], [0, 2], [5, 1], [3, 1]])
    list_of_coords.append([[0, 0], [0, 2], [3, 1], [5, 1]])
    list_of_coords.append([[0, 0], [2, 2], [6, 0], [3, 1]])
    list_of_coords.append([[6, 0], [5, 5], [4, 0], [5, 6]])
    list_of_coords.append([[0, 0], [1, 1], [3, 3], [2, 2]])
    list_of_coords.append([[0, 1], [1, 1], [3, 2], [2, 1]])
    list_of_coords.append([[9, 7], [2, 5], [5, 3], [2, 5]])
    list_of_coords.append([[10, 2], [1, 6], [7, 5], [10, 7]])
    list_of_coords.append([[5, 1], [0, 9], [0, 7], [0, 2]])

    for item in list_of_coords:
        print("Checking...")
        print(item)
        hit = bullet_and_wall(item)
        if hit:
            print("It's a hit!\n")
        else:
            print("Missed by a mile!\n")


if __name__ == '__main__':
    main()



