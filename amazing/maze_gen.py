#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   maze_gen.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/22 13:23:07 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/22 13:23:08 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import random
from utils import cell_from_hex, hex_for_cell, valid


# random path validator
def random_path(x, y, width, height, visited):
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
def dfs_maze(maze_init, maze_grid, visited):
    #random.seed(56)
    entry = maze_init.entry
    width = maze_init.width
    height = maze_init.height
    ex, ey = entry
    stack = [(ex, ey)]
    visited[ey][ex] = True

    while stack:
        x, y = stack[-1]
        result = random_path(x, y, width, height, visited)
        if result:
            vx, vy, directions = result
            carve_paths(x, y, vx, vy, directions, maze_grid)
            visited[vy][vx] = True
            stack.append((vx, vy))
            #output(maze_grid, entry, exit)
        else:
            stack.pop()

    return maze_grid

#generating entries
def entry_gen(visited, width, height):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    while  visited[y][x]:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
    return (x, y)


#walls to break
def walls_to_break(width, height):
    total_internal_walls = width * (height - 1) + height * (width - 1)
    percentage = random.randint(5, 7) / 100.0
    walls_break = max(1, int(total_internal_walls * percentage))

    return walls_break



#imperfect maze

def find_imp_paths(x, y, width, height, visited,  maze):
    dirs = []
    n,e,s,w = cell_from_hex(maze[y][x])

    if n == 1 and valid(x, y-1, width, height) and not visited[y-1][x]:
        if cell_from_hex(maze[y-1][x])[2] == 1:
            dirs.append((x, y-1, "N"))
    if e == 1 and valid(x+1, y, width, height)and not visited[y][x+1]:
        if cell_from_hex(maze[y][x+1])[3] == 1:
            dirs.append((x+1, y, "E"))
    if s == 1 and valid(x, y+1, width, height) and not visited[y+1][x]:
        if cell_from_hex(maze[y+1][x])[0] == 1:
            dirs.append((x, y+1, "S"))
    if w == 1 and valid(x-1, y, width, height) and not visited[y][x-1]:
        if cell_from_hex(maze[y][x-1])[1] == 1:
            dirs.append((x-1, y, "W"))

    if dirs:
        return random.choice(dirs)
    return None


#imperfect maze maker

def imperfect_maze_gen(maze_init, maze_grid, visited):
    width = maze_init.width
    height = maze_init.height
    walls_break = walls_to_break(width, height)

    while walls_break > 0:
        entry = entry_gen(visited, width, height)
        result = find_imp_paths(entry[0], entry[1], width, height, visited, maze_grid)
        if result:
            vx, vy, directions = result
            visited[vy][vx] = True
            carve_paths(entry[0], entry[1], vx, vy, directions, maze_grid)
            walls_break -= 1
    return maze_grid
