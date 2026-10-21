def detect_pos(coord): 

    x = 0
    y = 0                   # Returns the position of the square that is finded on the coordinates given.

    for i in range (1, 11):
        if coord[0] > 587 and coord[0] > (((i - 1) * 4) + ((i - 1) * 71) + 587) and coord[0] < (((i - 1) * 4) + (i * 71) + 587):
            x = i

    for i in range (1, 11):
        if coord[1] > 167 and coord[1] > (((i - 1) * 4) + ((i - 1) * 71) + 167) and coord[1] < (((i - 1) * 4) + (i * 71) + 167):
            y = i

    return (x, y)

def grid_create():
    grid_pos = []
    grid_coord = []
    grid = {}
    for i in range (1, 11):
        for j in range (1, 11):
            grid_pos.append((i, j))

    for i in range(0, 10):                                      # Creates grid dict that has positions as keys and coordinates as values
        for j in range(0, 10):                                  #       {(1, 1)         :         (587, 167)}
            grid_coord.append(                                  #      Position of           (x, y) of the topleft
                (                                               #        square               corner of the square
                    (591 + (i * 71) + ((i - 1) * 4)),
                    (171 + (j * 71) + ((j - 1) * 4))            
                )
            )
    for i in range(0, 100):
        grid[grid_pos[i]] = grid_coord[i]

    return grid

def map_create():
    map_pos = []
    map = {}
    for i in range (1, 11):
        for j in range (1, 11):
            map_pos.append((i, j))      # Creates an 8x8 grid map: {(1, 1) : "id"}
    for i in range (0, 100):
        map[map_pos[i]] = 0 
    
    return map

map = map_create()
grid = grid_create()