#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   utils.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/22 13:23:23 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/22 15:42:38 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from parsing import parse_config, get_config_values

try:
    cfg = parse_config("config.txt")
    width, height, entry, exit, output_file, perfect = get_config_values(cfg)
except Exception as e:
    print(f"{e}")
    exit(1)

#try:
#    width, height, entry, exit, output_file, perfect = get_config_values(cfg)
#except Exception as e:
#    print(f"ENTRY and EXIT must be in 'x,y' format with integers: {e}")
#    exit(1)

#try:
#    validate_config(width, height, entry, exit)
#except ValueError as e:
#    print(f"Config validation error: {e}")
#    exit(1)  # stop program safely



class Maze:
    def __init__(self, width, height, entry, exit, output_file, is_perfect):
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

maze_init = Maze(width, height, entry, exit, output_file, perfect)



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


#output file
def output(maze, maze_init, pathways):
    entry = maze_init.entry
    exit = maze_init.exit
    filename = maze_init.output_file
    output_file_t = []

    m = []
    path = []
    for v in maze:
        row = []
        for val in v:
            row.append(val)
        m.append("".join(row))

    path.append("".join(pathways))

    output_file_t.extend(m)
    output_file_t.append("")
    output_file_t.append(f"{entry[0]},{entry[1]}")
    output_file_t.append(f"{exit[0]},{exit[1]}")
    output_file_t.extend(path)

    res = "\n".join(output_file_t)
    #print(res)
    save_file(filename, res)




def save_file(filename: str, content: str) -> None:
    f = open(filename, "w")
    f.write(content)
    f.close()