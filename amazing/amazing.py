#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   amazing.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/22 13:22:53 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/22 15:25:15 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from utils import output, maze_init
from maze_gen import dfs_maze, imperfect_maze_gen
from maze_solver import dfs_maze_solver, bfs_shortest_path
import copy



# maze generation
def maze_generation (maze_grid, maze_init):
    height = maze_init.height
    width = maze_init.width
    entry = maze_init.entry
    exit = maze_init.exit
    x, y = entry
    a, b = exit
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
                    if (x == start_x + px and y == start_y + py) or (a == start_x + px and b == start_y + py):
                        raise Exception ("Entry and/or Exit are in the 42 wall pattern")
                    visited[start_y + py][start_x + px] = True
                else:
                    maze_grid[start_y + py][start_x + px] = 'F'

    return maze_grid


# cell creation
maze_grid= maze_init.generate_first_maze('F')
visited = maze_init.generate_first_maze(False)

try:
    perfect_maze = maze_generation(maze_grid, maze_init)
except Exception as e:
    print(f"{e}")
    exit(1)

maze_grid = perfect_maze
new_visited = copy.deepcopy(visited)
second_visited = copy.deepcopy(visited)

maze_gen = dfs_maze(maze_init, maze_grid, visited)


result_maze = []
print (maze_init.perfect)



#if not maze_init.perfect:
#    imperfect_maze = imperfect_maze_gen(maze_init, maze_gen, new_visited)
#    copy_imperfect = copy.deepcopy(imperfect_maze)
#    pathways_imp = dfs_maze_solver(maze_init, imperfect_maze, copy_imperfect, new_visited)
#    output(imperfect_maze, maze_init)
#    output(copy_imperfect, maze_init)
#    #print(pathways_imp)
#    print(imperfect_maze)
#else:
#    copy_m = copy.deepcopy(maze_gen)
#    ways = dfs_maze_solver(maze_init, maze_gen, copy_m,  new_visited)
#    output(maze_gen, maze_init)
#    output(copy_m, maze_init)
#    print(ways)

if not maze_init.perfect:
    result_maze = imperfect_maze_gen(maze_init, maze_gen, new_visited)
else:
    result_maze = maze_gen

shortest_path = True

if shortest_path:
    pathways = bfs_shortest_path(maze_init, result_maze, second_visited)
else:
    pathways = dfs_maze_solver(maze_init, result_maze, second_visited)

output(result_maze, maze_init, pathways)

#print(pathways)








