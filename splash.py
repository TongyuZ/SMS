'''
   This document is for creating a splash screen.

'''
import turtle
import time

# splash screen
screen = turtle.Screen()
screen.bgpic('./Resources/splash_screen.gif')
screen.title("CS5001 Sliding Puzzle Game")
screen.update()
time.sleep(2)
screen.clear()
# input name
player = screen.textinput("CS5001 Puzzle Slide", "Your Name:")

# input moving steps
moves = int(screen.numinput("5001 Puzzle Slide - Moves",
                            "Enter the number of moves you want [5-200]?",
                             default=50, minval=5, maxval=200))




