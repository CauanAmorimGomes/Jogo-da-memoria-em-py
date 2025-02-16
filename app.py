import turtle
import random

def draw_square(x, y, color_fill):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', color_fill)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

def draw_board():
    for i in range(16):
        x = (i % 4) * 60 - 90
        y = 90 - (i // 4) * 60
        draw_square(x, y, 'green')

def draw_tile(index):
    x = (index % 4) * 60 - 90
    y = 90 - (index // 4) * 60
    draw_square(x, y, 'white')
    turtle.up()
    turtle.goto(x + 15, y - 35)
    turtle.write(tiles[index], align="left", font=("Arial", 20, "normal"))

def hide_tiles(i, j):
    tile_state[i] = tile_state[j] = False
    draw_board()
    for k in range(16):
        if tile_state[k]:
            draw_tile(k)

def on_click(x, y):
    global first_tile
    for index in range(16):
        tile_x = (index % 4) * 60 - 90
        tile_y = 90 - (index // 4) * 60
        if tile_x <= x <= tile_x + 50 and tile_y - 50 <= y <= tile_y:
            if not tile_state[index]:
                tile_state[index] = True
                draw_tile(index)
                if first_tile is None:
                    first_tile = index
                else:
                    if tiles[first_tile] != tiles[index]:
                        screen.ontimer(lambda: hide_tiles(first_tile, index), 1000)
                    first_tile = None
            break

screen = turtle.Screen()
screen.bgcolor('yellow')
screen.title("Jogo da Memória")

tiles = list(range(8)) * 2
random.shuffle(tiles)
tile_state = [False] * 16
first_tile = None

draw_board()
screen.onclick(on_click)
screen.mainloop()
