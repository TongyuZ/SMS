'''
   This document is to draw the frames for sliders, leader board and buttons area.
'''

# sliders
def sliders_frame(frame_turtle):
    frame_turtle.speed(0)
    frame_turtle.ht()
    frame_turtle.up()
    frame_turtle.goto(-330, 300)
    frame_turtle.down()
    frame_turtle.pensize(3)
    frame_turtle.pencolor("black")
    frame_turtle.forward(410)
    frame_turtle.right(90)
    frame_turtle.forward(410)
    frame_turtle.right(90)
    frame_turtle.forward(410)
    frame_turtle.right(90)
    frame_turtle.forward(410)
    frame_turtle.right(90)

# leader board
def leaders_frame(frame_turtle):
    frame_turtle.speed(0)
    frame_turtle.ht()
    frame_turtle.up()
    frame_turtle.goto(100, 300)
    frame_turtle.down()
    frame_turtle.pensize(3)
    frame_turtle.pencolor("blue")
    frame_turtle.forward(210)
    frame_turtle.right(90)
    frame_turtle.forward(410)
    frame_turtle.right(90)
    frame_turtle.forward(210)
    frame_turtle.right(90)
    frame_turtle.forward(410)
    frame_turtle.right(90)
    frame_turtle.up()
    frame_turtle.goto(110,270)
    # load in leaders name list
    with open("leader.txt") as file:
        for line in file:
            frame_turtle.write(line.strip(), font=('Arial', 16, 'normal'))
            frame_turtle.goto(110, frame_turtle.ycor() - 18)

# button area
def buttons_frame(frame_turtle):
    frame_turtle.speed(0)
    frame_turtle.ht()
    frame_turtle.up()
    frame_turtle.goto(-330, -150)
    frame_turtle.down()
    frame_turtle.pensize(3)
    frame_turtle.pencolor("black")
    frame_turtle.forward(650)
    frame_turtle.right(90)
    frame_turtle.forward(100)
    frame_turtle.right(90)
    frame_turtle.forward(650)
    frame_turtle.right(90)
    frame_turtle.forward(100)
    frame_turtle.right(90)

def all_frames(frame_turtle):
    sliders_frame(frame_turtle)
    leaders_frame(frame_turtle)
    buttons_frame(frame_turtle)
