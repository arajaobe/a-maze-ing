
import random

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


#print("Maze width:", width)
#print("Maze height:", height)
#print("Entry:", entry)
#print("Exit:", exit)
#print("Output file:", output_file)
#print("Perfect maze:", perfect)
#print("Maze name:", name)
#print(cfg)

def hex_for_cell(north, east, south, west):
    """Convert wall booleans into hex digit."""
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

def generate_first_maze(width, height):
    maze = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append('F')
        maze.append(row)
    return maze

def generate_maze(width, height, entry, exit, perfect=True):
    maze = []
    entry_x, entry_y = entry
    exit_x, exit_y = exit
    for y in range(height):
        row = []
        for x in range(width):
            if (entry_x == x and entry_y == y) or (exit_x == x and exit_y == y):
                north = 0
                east  = 0
                south = 0
                west  = 0
            else:
            #north = random.randint(0, 1)
            #east  = random.randint(0, 1)
            #south = random.randint(0, 1)
            #west  = random.randint(0, 1)
                north = 1
                east  = 1
                south = 1
                west  = 1
            # WSEN
            row.append(hex_for_cell(north, east, south, west))
        maze.append(row)

    # Build output lines
    output = []
    output.extend(maze)
    #output.append(f"{entry[0]},{entry[1]}")
    #output.append(f"{exit[0]},{exit[1]}")
    #output.append("EESS")

    #return "\n".join(output)
    return maze

# Example usage with your config
#width, height = 3, 3
#entry, exit = (0,0), (2,2)
maze_text = generate_maze(width, height, entry, exit, perfect=True)
maze_first_text = generate_first_maze(width, height)

visited_cells = [[False for x in range(width)] for y in range(height)]

print(maze_text)

#print(maze_first_text)
print(visited_cells)

#n, e, s, w = cell_from_hex('3')
#print(f"{n} {e} {s} {w}")

#hexvalue = hex_for_cell(1, 1, 1 , 0)
#print(hexvalue)
#visited_cells = set()

#maze_text[1][0] = 'E'
#print(maze_text)

#print(visited_cells)

start_x = (width - 7) // 2
start_y = (height - 5) // 2

pattern = [
    ["4","4","4"," ","2","2","2"],
    [" "," ","4"," "," "," ","2"],
    ["4","4","4"," ","2","2","2"],
    ["4"," "," "," "," "," ","2"],
    ["4","4","4"," ","2","2","2"],
]


for py in range(5):
    for px in range(7):
        maze[start_y + py][start_x + px] = pattern[py][px]
