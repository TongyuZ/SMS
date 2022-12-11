'''
   This document is to help locate blank tile and swap tiles through valid clicks.
'''
import math
import Interface
import turtle

# check the location of blank tile
def loc_blank(file_dic):
    for i in range(1, len(file_dic) - 3):
        name = file_dic['name']
        number = file_dic['number']
        col_row = math.sqrt(int(number))
        if file_dic[str(i)] == f'Images/{name}/blank.gif':
            index_blank = i
    r = int(index_blank) // col_row
    c = int(index_blank) % col_row
    if c == 0:
        posit_blank = [-270 + (c + col_row - 1) * 98, 245 - (r - 1) * 98]
    else:
        posit_blank = [-270 + (c - 1) * 98, 245 - r * 98]
    return posit_blank, index_blank

# check the position of a click and whether or not it is valid
# a is the list of all clicks
a = []
file_dic = Interface.shuffle(Interface.read_image("mario.puz"))
sc_tile = turtle.Screen()
counter = 0
pen = turtle.Turtle()

def click_check(x, y, file_dic):
    # input the list of all clicks and the coordinate of current blank tile
    # locate the boundary of valid clicks
    # result is True when the clicked tile is adjacent to the blank tile
    global a
    a.append((x, y))
    global sc_tile
    global counter
    global pen
    posit_x = loc_blank(file_dic)[0][0]
    posit_y = loc_blank(file_dic)[0][1]
    index_blank = loc_blank(file_dic)[1]
    if -330 <= a[-1][0] <= 80 and -110 <= a[-1][1] <= 330:
        if posit_y - 98 / 2 <= a[-1][1] <= posit_y + 98 / 2:
            if posit_x - 49 - 98 <= a[-1][0] <= posit_x - 49 \
                    or posit_x + 49 <= a[-1][0] <= posit_x + 49 + 98:
                result = True
            else:
                result = False
        elif posit_x - 98 / 2 <= a[-1][0] <= posit_x + 98 / 2:
            if posit_y - 98 / 2 - 98 <= a[-1][1] <= posit_y - 98 / 2 \
                    or posit_y + 98 / 2 <= a[-1][1] <= posit_y + 98 / 2 + 98:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False

    # find the position of the clicked tiles
    number = int(file_dic["number"])
    base_x = -270 - 49
    base_y = 245 + 49
    cor_x = (a[-1][0] - base_x) // 98
    cor_y = (base_y - a[-1][1]) // 98
    index_a = int(math.sqrt(number) * cor_y + cor_x + 1)
    # if the result is True, the click is valid,
    # then swap the clicked tile and the blank one.
    if result:
        tile_swap = file_dic[str(index_a)]
        sc_tile.register_shape(tile_swap)
        tile_turtle = turtle.Turtle(shape=tile_swap)
        tile_turtle.penup()
        tile_turtle.speed(0)
        tile_turtle.goto(posit_x, posit_y)
        tile_turtle.stamp()
        tile_blank = file_dic[str(index_blank)]
        sc_tile.register_shape(tile_blank)
        tile_turtle = turtle.Turtle(shape=tile_blank)
        tile_turtle.penup()
        tile_turtle.speed(0)
        column_row = math.sqrt(number)
        r = int(index_a) // column_row
        c = int(index_a) % column_row
        if c == 0:
            tile_turtle.goto(-270 + (c + column_row - 1) * 98, 245 - (r - 1) * 98)
        else:
            tile_turtle.goto(-270 + (c - 1) * 98, 245 - r * 98)
        tile_turtle.stamp()
        file_dic[str(index_blank)] = file_dic[str(index_a)]
        name = file_dic['name']
        file_dic[str(index_a)] = f'Images/{name}/blank.gif'

