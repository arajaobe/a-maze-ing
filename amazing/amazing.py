

import random

#parsing

def parse_config(filename):
    config = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue
            key, value = line.split("=", 1)
            config[key] = value
    return config

cfg = parse_config("config.txt")

width = int(cfg["WIDTH"])
height = int(cfg["HEIGHT"])
entry = tuple(map(int, cfg["ENTRY"].split(",")))
exit = tuple(map(int, cfg["EXIT"].split(",")))
output_file = cfg["OUTPUT_FILE"]
perfect = cfg["PERFECT"].lower() == "true"


class Maze:
    def __init__(self, width, height, entry, exit, output_file, is_perfect=True):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = is_perfect

    #maze generation
    def generate_first_maze(self):
        maze = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append('F')
            maze.append(row)
        return maze


    #visited maze
    def visited_cells(self):
         return [[False for x in range(self.width)] for y in range(self.height)]

#hexa
def hex_for_cell(north, east, south, west):
    """Convert into hex digit."""
    value = (north << 0) | (east << 1) | (south << 2) | (west << 3)
    result = format(value, "X")
    return result

def cell_from_hex(hex_digit):
    """Convert hex digit into 4 wall bits (N, E, S, W)."""
    value = int(hex_digit, 16)  # convert hex string to integer

    north = (value >> 0) & 1
    east  = (value >> 1) & 1
    south = (value >> 2) & 1
    west  = (value >> 3) & 1

    return north, east, south, west



def valid(x, y, width, height):
    if (x >= 0 and x < width) and (y >= 0 and y < height):
        return True
    return False


#def random_path(current, visited, maze_grid):
#    x, y = current
#    hex_current = maze_grid[y][x]
#    nc, ec, sc, wc = cell_from_hex(hex_current)
#    stack = []
#    north = (x, y-1)
#    east = (x+1, y)
#    south = (x, y+1)
#    west = (x-1, y)

#    if valid(north):
#        if not visited[y-1][x]:
#            stack.append(north)
#    if valid(east):
#        if not visited[y][x+1]:
#            stack.append(east)
#    if valid(south):
#        if not visited[y+1][x]:
#            stack.append(south)
#    if valid(west):
#        if not visited[y][x-1]:
#            stack.append(west)
#    if stack:
#        result =  random.choice(stack)
#        a, b = result
#        new_cell = maze_grid[b][a]
#        n, e, s, w = cell_from_hex(new_cell)
#        if a == north[0] and b == north[1]:
#            nc = 0
#            s = 0
#        elif a == east[0] and b == east[1]:
#            ec = 0
#            w = 0
#        elif a == south[0] and b == south[1]:
#            sc = 0
#            n = 0
#        elif a == west[0] and b == west[1]:
#            wc = 0
#            e = 0
#        to_hex_current = hex_for_cell(nc, ec, sc, wc)
#        to_new_cell = hex_for_cell(n, e, s, w)
#        maze_grid[y][x] = to_hex_current
#        maze_grid[b][a] = to_new_cell
#        return result

#    return None




#def valid(x, y, width, height):
#    return 0 <= x < width and 0 <= y < height

#def random_path(current, visited, width, height, maze_grid):
#    x, y = current
#    neighbors = []

#    # North
#    nx, ny = x, y-1
#    if valid(nx, ny, width, height) and not visited[ny][nx]:
#        neighbors.append((nx, ny))

#    # East
#    nx, ny = x+1, y
#    if valid(nx, ny, width, height) and not visited[ny][nx]:
#        neighbors.append((nx, ny))

#    # South
#    nx, ny = x, y+1
#    if valid(nx, ny, width, height) and not visited[ny][nx]:
#        neighbors.append((nx, ny))

#    # West
#    nx, ny = x-1, y
#    if valid(nx, ny, width, height) and not visited[ny][nx]:
#        neighbors.append((nx, ny))

#    if neighbors:
#        return random.choice(neighbors)
#    return None


maze_init = Maze(width, height, entry, exit, output_file, perfect)

maze_grid= maze_init.generate_first_maze()

visited = maze_init.visited_cells()

def random_path(x, y, visited, width, height):
    neighbors = []
    directions = [(0, -1, "N"), (1, 0, "E"), (0, 1, "S"), (-1, 0, "W")]

    for dx, dy, d in directions:
        vx, vy = x + dx, y + dy
        if valid(vx, vy, width, height) and not visited[vy][vx]:
            neighbors.append((vx, vy, d))
    if neighbors:
        return random.choice(neighbors)
    return None



def carve_paths(x, y, vx, vy, directions, maze_grid):
    n, s, e, w = cell_from_hex(maze_grid[y][x])

    if directions == "N":
        n = 0
        nn, ns, ne, nw = cell_from_hex(maze_grid[vy][vx])
        ns = 0
        maze_grid[y][x] = hex_for_cell(n, s, e, w)
        maze_grid[vy][vx] = hex_for_cell(nn, ns, ne, nw)
    elif directions == "E":
        e = 0
        nn, ns, ne, nw = cell_from_hex(maze_grid[vy][vx])
        nw = 0
        maze_grid[y][x] = hex_for_cell(n, s, e, w)
        maze_grid[vy][vx] = hex_for_cell(nn, ns, ne, nw)
    elif directions == "S":
        s = 0
        nn, ns, ne, nw = cell_from_hex(maze_grid[vy][vx])
        nn = 0
        maze_grid[y][x] = hex_for_cell(n, s, e, w)
        maze_grid[vy][vx] = hex_for_cell(nn, ns, ne, nw)
    elif directions == "W":
        w = 0
        nn, ns, ne, nw = cell_from_hex(maze_grid[vy][vx])
        ne = 0
        maze_grid[y][x] = hex_for_cell(n, s, e, w)
        maze_grid[vy][vx] = hex_for_cell(nn, ns, ne, nw)



def dfs_maze(maze_grid, visited, entry, width, height):
    ex, ey = entry
    stack = [(ex, ey)]
    visited[ey][ex] = True

    while stack:
        x, y = stack[-1]
        result = random_path(x, y, visited, width, height)
        if result:
            vx, vy, directions = result
            carve_paths(x, y, vx, vy, directions, maze_grid)
            visited[vy][vx] = True
            stack.append((vx, vy))
        else:
            stack.pop()

    return maze_grid


#def dfs_maze(width, height, visited, entry, maze_grid):
#    stack = []
#    total = width * height
#    check_vist = 1

#    # start at (0,0)
#    x, y = entry
#    current = (x, y)
#    visited[y][x] = True
#    stack.append(current)

#    while stack:
#        result = random_path(current, visited, maze_grid)

#        if result:
#            x, y = result
#            current = (x, y)
#            stack.append(current)
#            visited[y][x] = True
#            check_vist += 1
#        else:
#            stack.pop()
#            if stack:
#                current = stack[-1]
#        print(visited)

#        if check_vist == total:
#            break


m = dfs_maze(maze_grid, visited, entry, width, height)


def generate_m_maze(m):
    maze = []
    for y in range(height):
        row = []
        for x in range(width):
            #print(m[x][y], end="")
            row.append(m[x][y])
        #row.append()
        maze.append("".join(row))
    return "\n".join(maze)


test = generate_m_maze(m)
print(visited)
print(test)