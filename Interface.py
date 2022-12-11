'''
   This document is to help display different groups of puzzles.
'''
import copy
import random
import turtle
import math

# shuffle the order of tiles
def shuffle(file_dic):
    tiles_copy = copy.deepcopy(file_dic)
    del tiles_copy['name']
    del tiles_copy['number']
    del tiles_copy['size']
    del tiles_copy['thumbnail']
    shuffled = list(tiles_copy.values())
    random.shuffle(shuffled)
    tiles_shuffled = dict(zip(tiles_copy, shuffled))
    for i in tiles_shuffled:
        file_dic[i] = tiles_shuffled[i]
    return file_dic


# read in file information
def read_image(file_name):
    # create a name list for each image of mario
    name_list = []
    with open(file_name) as image_mario:
        for item in image_mario:
            name_list.append(item)
    # split each string inside the list by colon
    # so that we get keys and values separated
    keys_values = [0] * len(name_list)
    for i in range(len(name_list)):
        keys_values[i] = name_list[i].split(":")
    # map the keys and values to make a dictionary
    # file dic contains all information about a puzzle set
    file_dic = dict()
    for j in range(len(keys_values)):
        file_dic[keys_values[j][0]] = keys_values[j][1].strip()
    return file_dic

''' 
    Description for "display()" function listed below:
        input the dictionary of a puzzle and specific screen object for tiles.
        file_dic has four descriptive information,
        but we only need image name when displaying tiles,
        so we just ignore them when displaying.
        The number of tiles is len(file_dic) - 4.
'''
def display(file_dic, sc_tile):
    num = file_dic['number']
    try:
        for keys in range(1, len(file_dic) - 4 + 1):
            tile_add = file_dic[str(keys)]
            sc_tile.register_shape(tile_add)
            tile_turtle = turtle.Turtle(shape=tile_add)
            tile_turtle.speed(0)
            tile_turtle.penup()
            # get the position of each tile, r stands for row, c for column
            # tile 1 is (0,0), tile 2 is (0,1)
            column_row = math.sqrt(int(num))
            r = int(keys) // column_row
            c = int(keys) % column_row
            if c == 0:
                tile_turtle.goto(-270 + (c + column_row - 1) * 98, 245 - (r - 1) * 98)
            else:
                tile_turtle.goto(-270 + (c - 1) * 98, 245 - r * 98)
            tile_turtle.stamp()
            tile_turtle.hideturtle()
        # display thumbnail
        tile_thumbnail = file_dic["thumbnail"]
        sc_tile.register_shape(tile_thumbnail)
        tile_turtle = turtle.Turtle(shape=tile_thumbnail)
        tile_turtle.penup()
        tile_turtle.speed(0)
        tile_turtle.goto(280, 280)
        tile_turtle.stamp()
        tile_turtle.hideturtle()
    except TypeError:
        print("It's a malformed file")
        warning = "./Resources/file_error.gif"
        reminder_sc = turtle.Screen()
        reminder_sc.register_shape(warning)
        reminder = turtle.Turtle(shape=warning)
        reminder.penup()
        reminder.speed(0)
        reminder.goto(0, 0)
        reminder.stamp()
        reminder.hideturtle()
        time.sleep(1)
        reminder.clear()


