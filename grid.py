
def map_create():
    map_pos = []
    map = {}
    for i in range (1, 9):
        for j in range (1, 9):
            map_pos.append((i, j))      # Creates an 8x8 grid map: {(1, 1) : "id"}
    for i in range (0, 32):
        map[map_pos[i]] = 0 
    
    return map

map = map_create()
print (map)   