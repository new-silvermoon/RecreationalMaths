"""Golden angle"""

import turtle
import time


head = turtle.Turtle()
head.hideturtle()
head.speed(3)
color = '#4caf50'
golden_angle = 137.5
head.color(color)

def draw_circle(x,y,radius):
    global head
    head.setheading(0)
    head.penup()
    head.fillcolor(color)
    head.goto(x, y-radius)
    head.begin_fill()
    head.circle(radius)
    head.end_fill()
    head.pendown()


draw_circle(0,0,10)

head.goto(0,0)
head.width(4)
head.setheading(90)

for leaf in range(50):
    head.forward(100)
    head.forward(-100)
    head.right(golden_angle)
    time.sleep(1)


