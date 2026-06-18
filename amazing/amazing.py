
from utils import output, maze_init
from maze_gen import dfs_maze, imperfect_maze_gen
from maze_solver import dfs_maze_solver, bfs_shortest_path
import copy


# maze generation
def maze_generation (maze_grid, maze_init):
    height = maze_init.height
    width = maze_init.width
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


# cell creation
maze_grid= maze_init.generate_first_maze('F')
visited = maze_init.generate_first_maze(False)


perfect_maze = maze_generation(maze_grid, maze_init)
maze_grid = perfect_maze
new_visited = copy.deepcopy(visited)

#maze = dfs_maze(maze_init, maze_grid, visited)



print (maze_init.perfect)

#if not maze_init.perfect:
#    imperfect_maze = imperfect_maze_gen(maze_init, m, new_visited)
#    copy_imperfect = copy.deepcopy(imperfect_maze)
#    pathways_imp = dfs_maze_solver(maze_init, imperfect_maze, copy_imperfect, new_visited)
#    output(imperfect_maze, maze_init)
#    output(copy_imperfect, maze_init)
#    #print(pathways_imp)
#    print(imperfect_maze)
#else:
#    copy_m = copy.deepcopy(m)
#    ways = dfs_maze_solver(maze_init, m, copy_m,  new_visited)
#    output(m, maze_init)
#    output(copy_m, maze_init)
#    print(ways)

#maze = imperfect_maze_gen(maze_init, m, new_visited)
#maze = [['D', '1', '5', '5', '3', '9', '3', '9', '1', '3'], ['9', '4', '3', '9', '6', 'E', 'C', '6', 'A', 'A'], ['A', 'F', 'A', 'C', '3', 'F', 'F', 'F', '8', '6'], ['A', 'F', 'C', '5', '4', '5', '7', 'F', 'C', '3'], ['A', 'F', 'F', 'F', 'B', 'F', 'F', 'F', '9', '2'], ['A', '9', '3', 'F', 'A', 'F', 'D', '5', '0', '2'], ['A', 'A', 'A', 'F', 'A', 'F', 'F', 'F', '8', '2'], ['A', '8', '4', '1', '0', '1', '5', '5', '2', 'A'], ['8', '4', '3', '8', '2', 'C', '3', '9', '6', 'A'], ['C', '5', '6', 'E', 'C', '5', '4', '6', 'D', '6']]
#maze = [['D', '3', 'D', '1', '5', '3', 'B', '9', '1', '3'], ['9', '4', '5', '4', '1', '4', '4', '6', 'A', 'A'], ['A', 'F', '9', '3', 'A', 'F', 'F', 'F', 'A', 'A'], ['A', 'F', 'C', '4', '0', '5', '7', 'F', 'A', 'E'], ['A', 'F', 'F', 'F', 'A', 'F', 'F', 'F', 'C', '3'], ['8', '1', '3', 'F', 'A', 'F', 'D', '5', '1', '2'], ['A', 'C', '6', 'F', 'A', 'F', 'F', 'F', 'A', 'A'], ['A', '9', '1', '3', 'C', '5', '1', '1', '6', 'A'], ['8', '6', '8', '0', '3', '9', '4', '0', '1', '2'], ['C', '5', '4', '6', 'C', '4', '5', '6', 'C', '6']]

#maze = [['D', '1', '1', '1', '3', '9', '5', '3', '9', '3'], ['9', '4', '0', '0', '4', '6', 'D', '4', '0', '2'], ['A', 'F', '8', '0', '3', 'F', 'F', 'F', 'A', 'A'], ['A', 'F', 'C', '4', '0', '5', '7', 'F', 'C', '2'], ['A', 'F', 'F', 'F', 'A', 'F', 'F', 'F', '9', '2'], ['A', '9', '3', 'F', 'A', 'F', 'D', '5', '0', '2'], ['C', '6', 'A', 'F', 'A', 'F', 'F', 'F', '8', '2'], ['9', '1', '0', '5', '0', '1', '1', '5', '0', '2'], ['8', '0', '0', '3', '8', '2', '8', '1', '0', '2'], ['C', '4', '4', '4', '4', '4', '4', '4', '4', '6']]

#maze  =[['B', '9', '3', '9', '1', '5', '7', '9', '1', '3'], ['A', 'E', 'A', 'A', 'C', '5', '5', '6', 'A', 'E'], ['A', 'F', 'A', 'C', '3', 'F', 'F', 'F', '8', '3'], ['A', 'F', 'C', '5', '0', '5', '7', 'F', 'A', 'A'], ['A', 'F', 'F', 'F', 'A', 'F', 'F', 'F', 'A', 'A'], ['A', '9', '7', 'F', 'A', 'F', 'D', '5', '2', 'A'], ['A', 'C', '3', 'F', 'E', 'F', 'F', 'F', 'E', 'A'], ['C', '3', '8', '5', '1', '3', 'D', '5', '1', '6'], ['B', 'A', 'C', '7', 'A', 'A', '9', '3', 'C', '3'], ['C', '4', '5', '5', '6', 'C', '6', 'C', '5', '6']]

#maze = [['D', '5', '3', '9', '5', '3', '9', '3', 'D', '3'], ['9', '5', '6', 'C', '3', 'C', '6', 'C', '3', 'A'], ['A', 'F', '9', '5', '6', 'F', 'F', 'F', 'A', 'A'], ['A', 'F', 'C', '5', '1', '5', '7', 'F', 'A', 'A'], ['A', 'F', 'F', 'F', 'A', 'F', 'F', 'F', 'C', '2'], ['C', '5', '3', 'F', 'A', 'F', 'D', '5', '1', '6'], ['9', '5', '6', 'F', 'A', 'F', 'F', 'F', 'A', 'B'], ['C', '5', '3', 'D', '2', '9', '3', 'B', 'A', 'A'], ['9', '3', 'A', '9', '6', 'A', 'C', '6', 'C', '2'], ['E', 'C', '4', '6', 'D', '4', '5', '5', '5', '6']]

maze = [['D', '5', '3', 'D', '5', '3', '9', '5', '1', '3'], ['9', '7', 'A', '9', '3', 'C', '4', '7', 'A', 'E'], ['A', 'F', 'A', 'A', 'A', 'F', 'F', 'F', 'C', '3'], ['A', 'F', 'C', '6', '8', '5', '7', 'F', '9', '2'], ['A', 'F', 'F', 'F', 'A', 'F', 'F', 'F', 'A', 'E'], ['C', '5', '3', 'F', 'A', 'F', 'D', '5', '0', '3'], ['9', '3', 'A', 'F', 'A', 'F', 'F', 'F', 'A', 'A'], ['A', 'C', '0', '7', 'C', '5', '5', '3', 'E', 'A'], ['A', 'D', '6', '9', '1', '5', '7', 'C', '3', 'A'], ['C', '5', '5', '6', 'C', '5', '5', '5', '4', '6']]

print(maze)
copy_maze = copy.deepcopy(maze)
#pathways= dfs_maze_solver(maze_init, maze, copy_maze, new_visited)
paths = bfs_shortest_path(maze_init, maze, copy_maze, new_visited)

output(maze, maze_init)
output(copy_maze, maze_init)

print (paths)
#print(pathways)




