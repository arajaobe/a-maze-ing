# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  mlx_2.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: samrazaf <samrazaf@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/23 00:38:34 by samrazaf        #+#    #+#               #
#  Updated: 2026/06/23 01:10:46 by samrazaf        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import mlx
from utils import width, height, entry, exit, cell_from_hex
from amazing import result_maze, maze_init, maze_gen, new_visited, imperfect_maze_gen

# Window dimensions (fixed)
w = 550
h = 550
thickness = 5
margin = 20

# Choose one uniform cell size (square cells)
cell_size = min((w - 2*margin) // width, (h - 2*margin) // height)
size_x = size_y = cell_size

# Maze dimensions in pixels
maze_w = width * cell_size
maze_h = height * cell_size

# Compute borders (center maze with padding)
border_x = (w - maze_w) // 2
border_y = (h - maze_h) // 2

class Draw:
    def __init__(self, m, ptr, win, pos_x, pos_y, side_x, side_y, color):
        self.m = m
        self.ptr = ptr
        self.win = win
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.side_x = side_x
        self.side_y = side_y
        self.color = color

    def draw_line_top(self):
        for j in range(thickness):
            for i in range(self.side_x):
                self.m.mlx_pixel_put(
                    self.ptr,
                    self.win,
                    self.pos_x + i,
                    self.pos_y + j,
                    self.color
                    )

    def draw_line_left(self):
        for j in range(thickness):
            for i in range(self.side_y):
                self.m.mlx_pixel_put(
                    self.ptr,
                    self.win,
                    self.pos_x,
                    self.pos_y + self.side_y - i,
                    self.color
                    )

    def draw_line_down(self):
        for j in range(thickness):
            for i in range(self.side_x):
                self.m.mlx_pixel_put(
                    self.ptr,
                    self.win,
                    self.pos_x + i + j,
                    self.pos_y + self.side_y + j,
                    self.color
                    )

    def draw_line_right(self):
        for j in range(thickness):
            for i in range(self.side_y):
                self.m.mlx_pixel_put(
                    self.ptr,
                    self.win,
                    self.pos_x + self.side_x + j,
                    self.pos_y + i,
                    self.color
                    )


    def draw_square(self, color_1, color_2, color_3, color_4):
        size_yy = int(size_y / 2)
        size_xx= int(size_x / 2)
        temp = self.color
        #square left top
        self.color = color_1
        for i in range(size_yy):
            for j in range(size_xx):
                self.m.mlx_pixel_put(
                        self.ptr,
                        self.win,
                        self.pos_x + i + thickness,
                        self.pos_y + j + thickness,
                        self.color
                    )
        #square right top
        self.color = color_2
        for i in range(size_yy):
            for j in range(size_xx):
                self.m.mlx_pixel_put(
                        self.ptr,
                        self.win,
                        self.pos_x + self.side_x - i,
                        self.pos_y + j + thickness,
                        self.color
                    )
        ##square right down
        self.color = color_3
        for i in range(size_xx):
            for j in range(size_yy):
                self.m.mlx_pixel_put(
                        self.ptr,
                        self.win,
                        self.pos_x + self.side_y - i,
                        self.pos_y + self.side_x - j,
                        self.color
                    )
        #square left down
        self.color = color_4
        for i in range(size_xx):
            for j in range(size_yy):
                self.m.mlx_pixel_put(
                    self.ptr,
                    self.win,
                    self.pos_x + i + thickness,
                    self.pos_y + self.side_y - j,
                    self.color
                )
        self.color = temp

class TraceSquare(Draw):
    def __init__(self, m, ptr, win, pos_x, pos_y, side_x, side_y, color, hex):
        super().__init__(m, ptr, win, pos_x, pos_y, side_x, side_y, color)
        self.hex = hex

    def square_part(self, _):
        if self.hex[0] == 1:
            super().draw_line_top()
        if self.hex[1] == 1:
            super().draw_line_right()
        if self.hex[2] == 1:
            super().draw_line_down()
        if self.hex[3] == 1:
            super().draw_line_left()
        if (self.hex[0] == 1 and self.hex[1]
            and self.hex[2] and self.hex[3]):
            super().draw_square(0xFF253614, 0xFF748596, 0xFF326598, 0xFF784512)


class TraceNextSquare(TraceSquare):
    def __init__(self, m, ptr, win, pos_x, pos_y, side_x, side_y, color, hex, number_x, number_y, maze):
        super().__init__(m, ptr, win, pos_x, pos_y, side_x, side_y, color, hex)
        self.number_x = number_x
        self.number_y = number_y
        self.maze = maze

    def square_all(self, _):
        base_x = self.pos_x
        base_y = self.pos_y
        for j in range(self.number_y):
            for i in range(self.number_x):
                value = str(self.maze[j][i])
                self.hex = cell_from_hex(value)
                x = self.pos_x = base_x + i * self.side_x
                y = self.pos_y = base_y + j * self.side_y
                self.draw_cell(x, y)

    def draw_cell(self, x, y):
        temp_x = self.pos_x
        temp_y = self.pos_y
        self.pos_x = x
        self.pos_y = y
        self.square_part(None)
        self.pos_x = temp_x
        self.pos_y = temp_y

    def draw_posit(self, x, y, color_1, color_2, color_3, color_4):
        temp_x = self.pos_x
        temp_y = self.pos_y
        self.pos_x = x
        self.pos_y = y
        super().draw_square(color_1, color_2, color_3, color_4)
        self.pos_x = temp_x
        self.pos_y = temp_y


C = {
    'W': 0xFFFFFFFF,
    'R': 0xFFFF2020,
    'B': 0xFF2020FF,
    'G': 0xFF20FF20,
    'Y': 0xFFFFFF20,
}



def convert_posit_to_pixel(draw, x, y, color_1, color_2, color_3, color_4):
    a = x * cell_size + margin
    b = y * cell_size + margin
    draw.draw_posit(a, b, color_1, color_2, color_3, color_4)

#def draw_move(maze):

#def maze_regen():
#    if not maze_init.perfect:
#        result_maze = imperfect_maze_gen(maze_init, maze_gen, new_visited)
#    else:
#        result_maze = maze_gen
#    return result_maze

def deal_key(key, ptr):
    print(f"Key pressed: {key}")
    if key == 99:
        m.mlx_loop_exit(ptr)
    #if key == 114:
    #    maze_regen()

def draw_enter_sort(draw):
    x1, y1 = entry
    x2, y2 = exit
    convert_posit_to_pixel(draw, x1, y1, C['G'], C['G'], C['G'], C['G'])
    convert_posit_to_pixel(draw, x2, y2, C['R'], C['R'], C['R'], C['R'])

m = mlx.Mlx()
ptr = m.mlx_init()

win = m.mlx_new_window(ptr, w, h, "A-maze-ing")
maze = result_maze
#if maze_regen():
#    maze = maze_regen()
# Start drawing at border offsets
test = TraceNextSquare(m, ptr, win, border_x, border_y, size_x, size_y,
                       0xFFFFFFFF, cell_from_hex('0'), width, height, maze)

#convert_posit_to_pixel(test, 2, 2, C['B'], C['G'], C['W'], C['R'])
draw_enter_sort(test)
m.mlx_key_hook(win, deal_key, ptr)
m.mlx_expose_hook(win, test.square_all, None)

m.mlx_loop(ptr)
