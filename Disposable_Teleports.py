#Currently unfinished
"""Greg McClellan
   Created: 8/12/13
   Las Edited: 8/12/13

   Program is given a string of 2 digit numbers, seperated by commas.
   The numbers represent 2 teleports that are connected to each other.
   There are 8 teleports total, and the idea is to start at 1, go through each
   teleport at least once, and then return to 1.
"""

def checkio(teleports_string):
    teleports = teleports_string.split(",")
    start, current = 1, 1
    route = '1'
    connections_used = []

    teleport_connections = [0 for x in range(8)]
    for item in teleports:
        teleport_connections[int(item[0]) - 1] += 1
        teleport_connections[int(item[1]) - 1] += 1

    teleports_by_connection = {1: 0, 2: 0, 3: 0, 4: 0,
                               5: 0, 6: 0, 7: 0, 8: 0}

    for i, item in enumerate(teleport_connections):
        teleports_by_connection[i+1] = item


    teleports_visited = [0 for x in range(8)]
    teleports_visited[0] = 1

    while current != 1 or not all_visited(teleports_visited):
        next_tp = next_move(teleports, teleports_by_connection, teleports_visited, connections_used, current, route)
        print("XXXXX")
        print("Current: ", current, " Next: ", next_tp)
        route += str(next_tp)
        print(route)
        print(teleports_by_connection)
        current = move(current, next_tp, teleports_visited, teleports_by_connection, connections_used)

    return route

def check_teleport(teleports, current_tp, next_tp, connections_used):
    #checks if you can teleport from current to next
    for item in teleports:

        if item[0] == str(current_tp) and item[1] == str(next_tp) or item[0] == str(next_tp) and item[1] == str(current_tp):

            for used in connections_used:
                if used[0] == str(current_tp) and used[1] == str(next_tp) or used[0] == str(next_tp) and used[1] == str(current_tp):
                    return False

            return True

    else:
        return False

def all_visited(teleports_visited):
    #Returns True once all teleports have been visited
    all_visited = True
    for item in teleports_visited:
        if item < 1:
            return False

    else:
        return True

def move(current_tp, next_tp, teleports_visited, teleports_by_connection, connections_used):
    #Carries out the movement from curent tp to next tp
    print("NEXT: ", next_tp)
    connections_used.append(str(current_tp) + str(next_tp))
    teleports_by_connection[current_tp] -= 1
    teleports_by_connection[next_tp] -= 1
    teleports_visited[next_tp - 1] += 1
    current_tp = next_tp
    return current_tp

def next_move(teleports, teleports_by_connection, teleports_visited, connections_used, current, route):
    #Decides which tp to travel to next
    print("VIsited: ", teleports_visited)
    if all_visited(teleports_visited): #if visited all tp's, tries to return home
        print("ALL_VISITED")
        if check_teleport(teleports, current, 1, connections_used):
            return 1

    for x in range(8, 1, -1):
        print("X = ", x)
        for i in range(2, 9):
            print("I = ", i)
            print("1st condition: ", teleports_by_connection[i] == x)
            print("2nd condition: ", check_teleport(teleports, current, i, connections_used))
            if teleports_by_connection[i] == x and check_teleport(teleports, current, i, connections_used):
                print("Returning: ", i)
                return i

    if teleports_by_connection[1] > 1 and check_teleport(teleports, current, 1, connections_used):
        return 1

    else:
        return False

map1 = "12,23,34,45,56,67,78,81"
map2 = "12,28,87,71,13,14,34,35,45,46,63,65"
map3 = "12,17,87,86,85,82,65,43,35,46"

print("done: ", checkio(map3))
            
               
