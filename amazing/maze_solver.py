#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   maze_solver.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/22 13:23:11 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/22 13:23:12 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from utils import cell_from_hex, valid
from collections import deque


# paths for the solver
def find_paths(x, y, visited, width, height,  maze):
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


#algo solver
def dfs_maze_solver(maze_init, new_maze_grid, visited):
    entry = maze_init.entry
    exit = maze_init.exit
    width = maze_init.width
    height = maze_init.height
    ex, ey = entry
    xx, xy = exit
    stack = [(ex, ey)]
    right_paths = []
    visited[ey][ex] = True

    while stack:
        x, y = stack[-1]
        result = find_paths(x, y, visited, width, height, new_maze_grid)
        if result:
            vx, vy, directions = result[0]
            right_paths.append(directions)
            visited[vy][vx] = True
            stack.append((vx, vy))
            if vx == xx and vy == xy:
                break
        else:
            stack.pop()

    return right_paths



# algo for the solver
#def dfs_maze_solver(maze_init, new_maze_grid, new_maze, visited):
#    entry = maze_init.entry
#    exit = maze_init.exit
#    width = maze_init.width
#    height = maze_init.height
#    ex, ey = entry
#    xx, xy = exit
#    stack = [(ex, ey)]
#    right_paths = []
#    visited[ey][ex] = True
#    new_maze[ey][ex] = "\033[42;37m.\033[0m"
#    new_maze[xy][xx] = "\033[41;37m.\033[0m"

#    while stack:
#        x, y = stack[-1]
#        result = find_paths(x, y, visited, width, height, new_maze_grid)
#        if result:
#            vx, vy, directions = result[0]
#            right_paths.append(directions)
#            #print(right_paths)
#            visited[vy][vx] = True
#            if directions == "N":
#                new_maze[vy][vx] = "\033[44;37m↑\033[0m"
#            elif directions == "E":
#                new_maze[vy][vx] = "\033[44;37m→\033[0m"
#            elif directions == "S":
#                new_maze[vy][vx] = "\033[44;37m↓\033[0m"
#            elif directions == "W":
#                new_maze[vy][vx] = "\033[44;37m←\033[0m"
#            stack.append((vx, vy))
#            #output(copy_m, entry, exit)
#            if vx == xx and vy == xy:
#                new_maze[vx][vy] = "\033[41;37m.\033[0m"
#                break
#        else:
#            stack.pop()

#    return right_paths


def bfs_shortest_path(maze_init, maze, visited):
    start = maze_init.entry
    end = maze_init.exit
    width = maze_init.width
    height = maze_init.height
    queue = deque([start])

    parent = {}
    visited[start[1]][start[0]] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break

        n, e, s, w = cell_from_hex(maze[y][x])
        directions = [("N", (x, y-1), n),
                      ("E", (x+1, y), e),
                      ("S", (x, y+1), s),
                      ("W", (x-1, y), w)]

        for dir, (nx, ny), wall in directions:
            if wall == 0:
                if valid(nx, ny, width, height) and not visited[ny][nx]:
                    visited[ny][nx] = True
                    parent[(nx, ny)] = (x, y, dir)
                    queue.append((nx, ny))

    # reconstruct path
    path = []
    #full_path = []
    cur = end
    while cur != start:
        px, py, dir = parent[cur]
        path.append(dir)
        #full_path.append((px, py, dir))
        cur = (px, py)
    path.reverse()
    #full_path.reverse()

    #for a, b , c in full_path:
    #    if c == "N":
    #        copy_maze[b][a] = "\033[44;37m↑\033[0m"
    #    elif c == "E":
    #        copy_maze[b][a] = "\033[44;37m→\033[0m"
    #    elif c == "S":
    #        copy_maze[b][a] = "\033[44;37m↓\033[0m"
    #    elif c == "W":
    #        copy_maze[b][a] = "\033[44;37m←\033[0m"

    return path
