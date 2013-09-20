"""Greg McClellan
   Created: 8/12/13
   Last Edited: 8/12/13

   Program will take a matrix of strings representing a rectangular map of 6 symbols.
    (G)Grass, (S)Shrubs can be landed on
    (R)Rocks, (W)Water, (T)Trees can not be landed on
   Program will return the largest rectangular area within map on which the spaceship can land
"""

def checkio(landing_map):
    landing_zone = 1

    for i, line in enumerate(landing_map):
        
        for j, unit in enumerate(line):
            
            if unit == 'G' or unit == 'S':
                x = largest_rectangle(landing_map, i, j)
                
                if x > landing_zone:
                    landing_zone = x

    return landing_zone

def largest_rectangle(landing_map, i, j):
    #Determines the largest rectangle available to land and containing index: (i, j) as its upper left corner
    x, y = 1, 1
    max_x, max_y = 0, 0
    area = 1

    for a in range(len(landing_map[0]) - j):
        if landing_map[i][j+a] == 'G' or landing_map[i][j+a] == 'S':
            max_x += 1
        else:
            break

    for a in range(len(landing_map) - i):
        if landing_map[i+a][j] == 'G' or landing_map[i+a][j] == 'S':
            max_y += 1
        else:
            break

    for x_val in range(max_x + 1):
        for y_val in range(max_y + 1):
            check = True
            check_area = 0
            for a in range(x_val):
                for b in range(y_val):
                    if landing_map[i + b][j + a] == 'G' or landing_map[i + b][j + a] == 'S':
                        check &= True
                        check_area += 1
                    else:
                        check &= False

            if check == True:
                if check_area > area:
                    area = check_area
            else:
                break

    return area

map1 = ['G']
map2 = ['GS',
        'GS']
map3 = ['GT',
        'GG']
map4 = ['GGTGG',
        'TGGGG',
        'GSSGT',
        'GGGGT',
        'GWGGG',
        'RGTRT',
        'RTGWT',
        'WTWGR']




print(checkio(map4))

        
                
