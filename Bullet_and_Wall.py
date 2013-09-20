class Coordinate(object):
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    def __repr__(self):
        return "(%.2f, %.2f)" %(self.x, self.y)

class Line(object):
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def __repr__(self):
        return "y = %.2fx + %.2f" %(self.m, self.b)

    def intersect(self, other_line):
        #checks if line intersects with another line given as input
        if type(other_line) == VerticalLine:
            return other_line.intersect(self)
        if self.m == other_line.m:
            if self.b == other_line.b:
                return Coordinate([self.b, 0])
            else:
                return False

        else:
            x = round((other_line.b - self.b)/(self.m - other_line.m), 4)
            y = round((self.m * x + self.b), 4)
            return Coordinate([x, y])

class VerticalLine(Line):
    def __init__(self, x_inter):
        self.x_inter = x_inter

    def __repr__(self):
        return "Vertical line intersects x-axis at %s" %(self.x_inter)

    def intersect(self, other_line):
        y = other_line.m*self.x_inter + other_line.b
        return Coordinate([self.x_inter, y])

def create_line(coord1, coord2):
    #Returns a line passing through 2 coordinates

    if coord1.x == coord2.x:
        return VerticalLine(coord1.x)
    
    else:
        m = (coord1.y - coord2.y)/(coord1.x - coord2.x)
        b = coord1.y - m * coord1.x
        return Line(m, b)

    


def bullet_and_wall(list_of_coords):
    #input is a list of four tuples containing coords to the 2 endpoints of wall and 2 coords of the bullet, the
    #first of which is its starting point
    w1, w2 = Coordinate(list_of_coords[0]), Coordinate(list_of_coords[1])
    a, b = Coordinate(list_of_coords[2]), Coordinate(list_of_coords[3])

    wall_line = create_line(w1, w2)
    bullet_line = create_line(a, b)

    intersect = wall_line.intersect(bullet_line)

    if w1.x == w2.x:
        if b.x >= a.x and w1.x < a.x and w2.x < a.x:
            return False
        elif b.x <= a.x and w1.x > a.x and w2.x > a.x:
            return False
            

    if intersect:
        if intersect.y > w1.y and intersect.y > w2.y:
            return False
        elif intersect.y < w1.y and intersect.y < w2.y:
            return False
        elif intersect.x > w1.x and intersect.x > w2.x:
            return False
        elif intersect.x < w1.x and intersect.x < w2.x:
            return False


        if b.x > a.x:
            if a.x > intersect.x:
                return False
        elif b.x < a.x:
            if a.x < intersect.x:
                return False
        else:
            if b.y > a.y:
                if a.y > intersect.y:
                    return False
            elif b.y < a.y:
                if a.y < intersect.y:
                    return False

    if intersect:
        return True
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
list_of_coords1 = [[0, 0], [0, 2], [5, 1], [3, 1]]
list_of_coords2 = [[0, 0], [0, 2], [3, 1], [5, 1]]
list_of_coords3 = [[0, 0], [2, 2], [6, 0], [3, 1]]
list_of_coords4 = [[6, 0], [5, 5], [4, 0], [5, 6]]
list_of_coords5 = [[0, 0], [1, 1], [3, 3], [2, 2]]
list_of_coords6 = [[0, 1], [1, 1], [3, 2], [2, 1]]
list_of_coords7 = [[9, 7], [2, 5], [5, 3], [2, 5]]
list_of_coords8 = [[10, 2], [1, 6], [7, 5], [10, 7]]
list_of_coords9 = [[5, 1], [0, 9], [0, 7], [0, 2]]

print(bullet_and_wall(list_of_coords9))




