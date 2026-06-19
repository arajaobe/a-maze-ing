import mlx
from utils import width, height


w = 720
h = 720

c1 = int(w / width)
c2 = int(h / height)


def deal_key(key, ptr):
    print(f"Key pressed: {key}")
    if key == 99:
        m.mlx_loop_exit(ptr)

#def draw_square(m, ptr, win, x, y, size, color):
#    for py in range(y, y + size):
#        for px in range(x, x + size):
#            m.mlx_pixel_put(ptr, win, px, py, color)

#def on_expose(win):
#    draw_square(m, ptr, win, 10, 10, 50, 0xFFFFFFFF)
#    m.mlx_pixel_put(ptr, win, 100, 100, 0xFF000000)


def new_square(win):
    x = 20
    y = 20
    for i in range(width):
        draw_square(m, ptr, win, x + c1 * i, y, c1, c2)


def draw_square(m, ptr, win, x, y, c1, c2):
    draw_line_top(m, ptr, win, x, y, c1, 0xFFFFFFFF)
    draw_line_down(m, ptr, win,x, y, c1, 0xFFFFFFFF)
    draw_line_left(m, ptr, win, x, y, c2, 0xFFFFFFFF)
    draw_line_rigth(m, ptr, win, x, y, c2, 0xFFFFFFFF)

    #m.mlx_pixel_put(ptr, win, 100, 100, 0xFF000000)

def draw_line_top(m, ptr, win, x, y, size, color):
    for i in range(size):
        m.mlx_pixel_put(ptr, win, x + i, y, color)

def draw_line_left(m, ptr, win, x, y, size, color):
    for i in range(size):
        m.mlx_pixel_put(ptr, win, x, y + size - i, color)

def draw_line_down(m, ptr, win, x, y, size, color):
    for i in range(size):
        m.mlx_pixel_put(ptr, win, x + i, y + size, color)

def draw_line_rigth(m, ptr, win, x, y, size, color):
    for i in range(size):
        m.mlx_pixel_put(ptr, win, x + size, y + i, color)
#if __name__ == "__main__":

m = mlx.Mlx()
ptr = m.mlx_init()
#if not width:
#    width = 720
#if not height:
#    height = 720
win = m.mlx_new_window(ptr, 780, 780, "Test 42")
m.mlx_key_hook(win, deal_key, ptr)
m.mlx_expose_hook(win, new_square, win)  # dessiner au bon moment

m.mlx_loop(ptr)
