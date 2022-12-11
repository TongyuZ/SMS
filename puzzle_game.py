'''
   This document is to help shift tiles.
   First, there are 4 cases when you are running the game(leave alone quit button)

   1. reset current game
   2. load another game
   3. continue run the current game
   4. quit the game

   So I'm going to break down the problem into 4 parts
   and create a list to keep track of where the user clicks
   and slide the puzzle as he/she expects.
'''
import time
import turtle
from Interface import read_image, display, shuffle
import swap
from Buttons import all_buttons
from gameboard import all_frames
import splash
import os

# get file name in the current directory
all_files = os.listdir()
file_split = []
for each in all_files:
    file_split.append(each.split("."))
# puzzle_file contains file name of each puzzle
puzzle_file = []
for i in range(len(file_split)):
    if len(file_split[i]) == 2:
        if file_split[i][1] == "puz":
            puzzle_file.append(file_split[i][0])
for i in range(len(puzzle_file)):
    puzzle_file[i] = puzzle_file[i] + ".puz"

# initialize some variables
basic_screen = turtle.Screen()
frame_turtle = turtle.Turtle()
sc_tile = turtle.Screen()
tile_turtle = turtle.Turtle()
# a is the list of all positions of clicks
a = []
# count is used to record the number of valid clicks
counter = 0
# pen is used to write the moving steps
pen = turtle.Turtle()
pen.speed(0)
# moves limits the maximum steps
moves = splash.moves

# default puzzle is mario
file_dic = shuffle(read_image("mario.puz"))
file_name = "mario.puz"

# swap or not swap tiles under user's instruction
def shift(x, y):
    global sc_tile
    global tile_turtle
    global a
    a.append((x, y))
    global file_dic
    global file_name
    global counter
    global pen
    # click rest button
    if (a[-1][0] - 50) ** 2 + (a[-1][1] + 200) ** 2 <= 2500:
        file_dic = read_image(file_name)
        display(file_dic, sc_tile)
        swap.click_check(x, y, file_dic)
        counter = 0
        pen.clear()
        pen.ht()
        pen.penup()
        pen.goto(-300, -180)
        pen.write(f"Moving Steps:{counter} ", move=False, align="left", font=("left", 18, "normal"))

    # click load button
    elif 110 <= a[-1][0] <= 190 and -240 <= a[-1][1] <= -160:
        file_name = sc_tile.textinput("Reload a new game you wanna play", f"{puzzle_file}")
        try:
            file_dic = shuffle(read_image(file_name))
            sc_tile.clear()
            all_buttons(basic_screen)
            all_frames(frame_turtle)
            display(file_dic, sc_tile)
            swap.click_check(x,y, file_dic)
            counter = 0
            pen.clear()
            pen.ht()
            pen.penup()
            pen.goto(-300, -180)
            pen.write(f"Moving Steps:{counter} ", move=False, align="left", font=("left", 18, "normal"))
        except FileNotFoundError:
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
    # click tiles
    elif -330 <= a[-1][0] <= 80 and -110 <= a[-1][1] <= 330:
        swap.click_check(x, y, file_dic)
        name = file_dic['name']
        pen.clear()
        pen.ht()
        pen.penup()
        pen.goto(-300, -180)
        counter = counter + 1
        pen.write(f"Moving Steps:{counter} ", move=False, align="left", font=("left", 18, "normal"))
        ordered_file = read_image(f'{name}.puz')
        reminder_sc = turtle.Screen()
        # win the game with steps remaining
        if 1 < counter < moves and file_dic == ordered_file:
            win = "./Resources/winner.gif"
            reminder_sc.register_shape(win)
            reminder = turtle.Turtle(shape=win)
            reminder.penup()
            reminder.speed(0)
            reminder.goto(0, 0)
            reminder.stamp()
            reminder.hideturtle()
            time.sleep(2)
            reminder.clear()
            credit = "./Resources/credits.gif"
            reminder_sc.register_shape(credit)
            reminder = turtle.Turtle(shape=credit)
            reminder.penup()
            reminder.speed(0)
            reminder.goto(0, 0)
            reminder.stamp()
            reminder.hideturtle()
            time.sleep(2)
            turtle.bye()
        # moves have been used up
        elif counter >= moves:
            lose = "./Resources/Lose.gif"
            reminder_sc.register_shape(lose)
            reminder = turtle.Turtle(shape=lose)
            reminder.penup()
            reminder.speed(0)
            reminder.goto(0, 0)
            reminder.stamp()
            time.sleep(2)
            reminder.hideturtle()
            reminder.clear()
            credit = "./Resources/credits.gif"
            reminder_sc.register_shape(credit)
            reminder = turtle.Turtle(shape=credit)
            reminder.penup()
            reminder.speed(0)
            reminder.goto(0, 0)
            reminder.stamp()
            reminder.hideturtle()
            time.sleep(2)
            turtle.bye()
    # click quit button
    elif 210 <= a[-1][0] <= 290 and -225 <= a[-1][1] <= -175:
        reminder_sc = turtle.Screen()
        quit_game = "./Resources/quitmsg.gif"
        reminder_sc.register_shape(quit_game)
        reminder = turtle.Turtle(shape=quit_game)
        reminder.penup()
        reminder.speed(0)
        reminder.goto(0, 0)
        reminder.stamp()
        reminder.hideturtle()
        time.sleep(2)
        reminder.clear()
        credit = "./Resources/credits.gif"
        reminder_sc.register_shape(credit)
        reminder = turtle.Turtle(shape=credit)
        reminder.penup()
        reminder.speed(0)
        reminder.goto(0, 0)
        reminder.stamp()
        reminder.hideturtle()
        time.sleep(2)
        turtle.bye()

# click handler
def my_handler(x, y):
    sc_tile.onscreenclick(None)
    shift(x,y)
    sc_tile.onscreenclick(my_handler)

# run game
def main():
    # draw three areas
    all_frames(frame_turtle)
    # draw buttons
    all_buttons(basic_screen)
    # draw tiles
    display(file_dic, sc_tile)
    # shift slides in terms of clicks
    sc_tile.onscreenclick(my_handler)
    turtle.done()

if __name__ == "__main__":
    main()


