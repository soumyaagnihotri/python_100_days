from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    r_c = (r, g, b)
    return r_c
angle = [90, 180, 270, 0]

tim.speed(0)
angle =0
for x in range(72):
    tim.color(random_color())
    angle +=5
    tim.setheading(angle)
    tim.circle(100)
screen = Screen()
screen.exitonclick()

