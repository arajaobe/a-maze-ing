

import random
import copy

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
    def generate_first_maze(self, value):
        maze = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(value)
            maze.append(row)
        return maze

    #visited maze
    #def visited_cells(self):
    #     return [[False for x in range(self.width)] for y in range(self.height)]

#Convert into hex digit
def hex_for_cell(north, east, south, west):
    value = (north << 0) | (east << 1) | (south << 2) | (west << 3)
    result = format(value, "X")
    return result

#Convert hex digit into 4 wall bits
def cell_from_hex(hex_digit):
    value = int(hex_digit, 16)  # convert hex string to integer

    north = (value >> 0) & 1
    east  = (value >> 1) & 1
    south = (value >> 2) & 1
    west  = (value >> 3) & 1

    return north, east, south, west


# cell validation
def valid(x, y, width, height):
    if (x >= 0 and x < width) and (y >= 0 and y < height):
        return True
    return False

# cell creation
maze_init = Maze(width, height, entry, exit, output_file, perfect)
maze_grid= maze_init.generate_first_maze('F')
visited = maze_init.generate_first_maze(False)

#output file
def output(maze, entry, exit):
    for value in maze:
        print("".join(value))
    print("\n")
    print(f"{entry[0]},{entry[1]}")
    print(f"{exit[0]},{exit[1]}")


# maze generation
def maze_generation (maze_grid, width, height):
    if width >= 9 and height >= 7:
        start_x = (width - 7) // 2
        start_y = (height - 5) // 2

        pattern = [
        ["F"," "," "," ","F","F","F"],
        ["F"," "," "," "," "," ","F"],
        ["F","F","F"," ","F","F","F"],
        [" "," ","F"," ","F"," "," "],
        [" "," ","F"," ","F","F","F"],
        ]

        for py in range(5):
            for px in range(7):
                maze_grid[start_y + py][start_x + px] = pattern[py][px]

        for py in range(5):
            for px in range(7):
                if maze_grid[start_y + py][start_x + px] == 'F':
                    visited[start_y + py][start_x + px] = True
                else:
                    maze_grid[start_y + py][start_x + px] = 'F'

    return maze_grid


#print(maze_grid)
modif = maze_generation(maze_grid, width, height)
output(modif, entry, exit)
maze_grid = modif
new_visited = copy.deepcopy(visited)
#print(new_visited)
new_maze_grid = maze_grid
#print(visited)



# random path validator
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



# carving the hexa paths
def carve_paths(x, y, vx, vy, directions, maze_grid):
    n, e, s, w = cell_from_hex(maze_grid[y][x])

    if directions == "N":
        n = 0
        nn, ne, ns, nw = cell_from_hex(maze_grid[vy][vx])
        ns = 0
        maze_grid[y][x] = hex_for_cell(n, e, s, w)
        maze_grid[vy][vx] = hex_for_cell(nn, ne, ns, nw )
    elif directions == "E":
        e = 0
        nn, ne, ns, nw = cell_from_hex(maze_grid[vy][vx])
        nw = 0
        maze_grid[y][x] = hex_for_cell(n, e, s, w)
        maze_grid[vy][vx] = hex_for_cell(nn, ne, ns, nw )
    elif directions == "S":
        s = 0
        nn, ne, ns, nw = cell_from_hex(maze_grid[vy][vx])
        nn = 0
        maze_grid[y][x] = hex_for_cell(n, e, s, w)
        maze_grid[vy][vx] = hex_for_cell(nn, ne, ns, nw )
    elif directions == "W":
        w = 0
        nn, ne, ns, nw = cell_from_hex(maze_grid[vy][vx])
        ne = 0
        maze_grid[y][x] = hex_for_cell(n, e, s, w)
        maze_grid[vy][vx] = hex_for_cell(nn, ne, ns, nw )


# algo for making the maze
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
            #output(maze_grid, entry, exit)
        else:
            stack.pop()

    return maze_grid

m = dfs_maze(maze_grid, visited, entry, width, height)

copy_m = copy.deepcopy(m)


# paths for the solver
def find_paths(x, y, visited, width, height, maze):
    dirs = []
    n,e,s,w = cell_from_hex(maze[y][x])

    if n == 0 and valid(x, y-1, width, height) and not visited[y-1][x]:
        if cell_from_hex(maze[y-1][x])[2] == 0:
            dirs.append((x, y-1, "N"))
    if e == 0 and valid(x+1, y, width, height)and not visited[y][x+1]:
        if cell_from_hex(maze[y][x+1])[3] == 0:
            dirs.append((x+1, y, "E"))
    if s == 0 and valid(x, y+1, width, height) and not visited[y+1][x]:
        if cell_from_hex(maze[y+1][x])[0] == 0:
            dirs.append((x, y+1, "S"))
    if w == 0 and valid(x-1, y, width, height) and not visited[y][x-1]:
        if cell_from_hex(maze[y][x-1])[1] == 0:
            dirs.append((x-1, y, "W"))

    return dirs


# algo for the solver
def dfs_maze_solver(new_maze_grid, new_maze, visited, entry, exit, width, height):
    ex, ey = entry
    xx, xy = exit
    stack = [(ex, ey)]
    right_paths = []
    visited[ey][ex] = True
    new_maze[ey][ex] = "\033[42;37m.\033[0m"
    new_maze[xy][xx] = "\033[41;37m.\033[0m"

    while stack:
        x, y = stack[-1]
        result = find_paths(x, y, visited, width, height, new_maze_grid)
        if result:
            vx, vy, directions = result[0]
            right_paths.append(directions)
            #print(right_paths)
            visited[vy][vx] = True
            if directions == "N":
                new_maze[vy][vx] = "\033[44;37m↑\033[0m"
            elif directions == "E":
                new_maze[vy][vx] = "\033[44;37m→\033[0m"
            elif directions == "S":
                new_maze[vy][vx] = "\033[44;37m↓\033[0m"
            elif directions == "W":
                new_maze[vy][vx] = "\033[44;37m←\033[0m"
            stack.append((vx, vy))
            #output(copy_m, entry, exit)
            if vx == xx and vy == xy:
                new_maze[vx][vy] = "\033[41;37m.\033[0m"
                break
        else:
            stack.pop()

    return right_paths

ways = dfs_maze_solver(m, copy_m,  new_visited, entry, exit, width, height)
#print(new_visited)


output(m, entry, exit)
output(copy_m,entry, exit)
print(ways)
