import mlx
from utils import width, height, cell_from_hex
from amazing import result_maze

# Window dimensions (fixed)
w = 1080
h = 720

margin = 100

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
        for i in range(self.side_x):
            self.m.mlx_pixel_put(self.ptr, self.win, self.pos_x + i, self.pos_y, self.color)

    def draw_line_left(self):
        for i in range(self.side_y):
            self.m.mlx_pixel_put(self.ptr, self.win, self.pos_x, self.pos_y + self.side_y - i, self.color)

    def draw_line_down(self):
        for i in range(self.side_x):
            self.m.mlx_pixel_put(self.ptr, self.win, self.pos_x + i, self.pos_y + self.side_y, self.color)

    def draw_line_right(self):
        for i in range(self.side_y):
            self.m.mlx_pixel_put(self.ptr, self.win, self.pos_x + self.side_x, self.pos_y + i, self.color)

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

def deal_key(key, ptr):
    print(f"Key pressed: {key}")
    if key == 99: 
        m.mlx_loop_exit(ptr)
    if key == 32:
        m.mlx_expose_hook(win, test.square_all, None)

m = mlx.Mlx()
ptr = m.mlx_init()

win = m.mlx_new_window(ptr, w, h, "A-maze-ing")
maze = result_maze

# Start drawing at border offsets
test = TraceNextSquare(m, ptr, win, border_x, border_y, size_x, size_y,
                       0xFFFFFFFF, cell_from_hex('0'), width, height, maze)

m.mlx_key_hook(win, deal_key, ptr)
m.mlx_expose_hook(win, test.square_all, None)

m.mlx_loop(ptr)
