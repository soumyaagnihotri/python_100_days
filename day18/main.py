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
tim.width(10)
tim.speed(10)
for x in range(100):
    tim.color(random_color())
    tim.setheading(random.choice(angle))
    tim.forward(35)
