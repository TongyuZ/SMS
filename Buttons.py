'''
   This document is to place three buttons.
'''

import turtle

# reset
def reset(screen):
    reset_button = "./Resources/resetbutton.gif"
    screen.register_shape(reset_button)
    buttons_r = turtle.Turtle(shape=reset_button)
    buttons_r.speed(0)
    buttons_r.penup()
    buttons_r.goto(50, -200)
    buttons_r.stamp()
    buttons_r.hideturtle()

# load
def load(screen):
    load_button = "./Resources/loadbutton.gif"
    screen.register_shape(load_button)
    buttons_l = turtle.Turtle(shape=load_button)
    buttons_l.speed(0)
    buttons_l.penup()
    buttons_l.goto(150, -200)
    buttons_l.stamp()
    buttons_l.hideturtle()

# quit
def quit(screen):
    quit_button = "./Resources/quitbutton.gif"
    screen.register_shape(quit_button)
    buttons_q = turtle.Turtle(shape=quit_button)
    buttons_q.speed(0)
    buttons_q.penup()
    buttons_q.goto(250, -200)
    buttons_q.stamp()
    buttons_q.hideturtle()


def all_buttons(screen):
    reset(screen)
    load(screen)
    quit(screen)