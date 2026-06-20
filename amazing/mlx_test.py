import mlx
from utils import width, height, cell_from_hex
from amazing import result_maze

#width = 2
#height = 3
w = 400
h = 400


#import mlx

#win = mlx.Window(400, 300, "MLX Test")

## Register a key handler
#def on_key(key):
#    print("Key pressed:", key)
#    if key == mlx.Key.ESCAPE:   # Escape key
#        win.close()

#win.on_key(on_key)

#while win.is_open():
#    win.clear(mlx.Color.BLACK)
#    win.draw_rect(50, 50, 100, 100, mlx.Color.RED)
#    win.update()


size_x = int(w / width)
size_y = int(h / height)

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

    def draw_block(self):
        for i in range(self.side_x - 5):
            for j in range(self.side_y - 5):
                self.m.mlx_pixel_put(self.ptr, self.win, self.pos_x + i, self.pos_y + j, self.color)
#def draw_square(m, ptr, win, x, y, size, color):
#    for py in range(y, y + size):
#        for px in range(x, x + size):
#            m.mlx_pixel_put(ptr, win, px, py, color)

#def on_expose(win):
#    draw_square(m, ptr, win, 10, 10, 50, 0xFFFFFFFF)
#    m.mlx_pixel_put(ptr, win, 100, 100, 0xFF000000)


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


    #def draw_enter(self, _):
    #    new_pos_y = 0
    #    new_pos_x = 0
    #    for i  new_pos_y == self.pos_y:
    #        if new_pos_x == self.pos_x:
    #            self.color = 0xFF00FF00
    #            super().draw_block()
    #            return
    #        else:
    #            self.draw_enter(new_pos_x + 1, new_pos_y)
    #    else:
    #        new_pos_x = 0
    #        self.draw_enter(new_pos_x, new_pos_y + 1)




#    def draw_block(self):
#        for i in range()

#    def color_all(self):


#    def color_enter(self):


def deal_key(key, ptr):
    print(f"Key pressed: {key}")
    if key == 99:
        m.mlx_loop_exit(ptr)
    if key == 32:
        m.mlx_expose_hook(win, test.draw_enter, None)


#def part_square(win):
#    x = 20
#    y = 20
#    c1 = 20
#    c2 = 20
#    hex = cell_from_hex("B")
#    square_part(m, ptr, win, x, y, c1, c2, hex)

#def new_square(win):
#    x = 20
#    y = 20
#    for i in range(width):
#        draw_square(m, ptr, win, x + c1 * i, y, c1, c2)

#def on_expose(win):
#    test.square_all()
#    test.draw_enter()
#def draw_square(m, ptr, win, x, y, c1, c2):
#    draw_line_top(m, ptr, win, x, y, c1, 0xFFFFFFFF)
#    draw_line_down(m, ptr, win,x, y, c1, 0xFFFFFFFF)
#    draw_line_left(m, ptr, win, x, y, c2, 0xFFFFFFFF)
#    draw_line_rigth(m, ptr, win, x, y, c2, 0xFFFFFFFF)

    #m.mlx_pixel_put(ptr, win, 100, 100, 0xFF000000)

#if __name__ == "__main__":

m = mlx.Mlx()
ptr = m.mlx_init()
#if not width:
#    width = 720
#if not height:
#    height = 720
win = m.mlx_new_window(ptr, 550, 550, "A-maze-ing")
#maze = [['D', '5', '3', 'D', '5', '3', '9', '5', '1', '3'], ['9', '7', 'A', '9', '3', 'C', '4', '7', 'A', 'E'], ['A', 'F', 'A', 'A', 'A', 'F', 'F', 'F', 'C', '3'], ['A', 'F', 'C', '6', '8', '5', '7', 'F', '9', '2'], ['A', 'F', 'F', 'F', 'A', 'F', 'F', 'F', 'A', 'E'], ['C', '5', '3', 'F', 'A', 'F', 'D', '5', '0', '3'], ['9', '3', 'A', 'F', 'A', 'F', 'F', 'F', 'A', 'A'], ['A', 'C', '0', '7', 'C', '5', '5', '3', 'E', 'A'], ['A', 'D', '6', '9', '1', '5', '7', 'C', '3', 'A'], ['C', '5', '5', '6', 'C', '5', '5', '5', '4', '6']]
maze = result_maze
#maze = [['A', 'B', 'C'], ['A', 'C', 'D'], ['B', 'D', 'E']]
test = TraceNextSquare(m, ptr, win, 75, 50, size_x, size_y, 0xFFFFFFFF, cell_from_hex('0'), width, height, maze)
m.mlx_key_hook(win, deal_key, ptr)
m.mlx_expose_hook(win, test.square_all, None)  # dessiner au bon moment

m.mlx_loop(ptr)
