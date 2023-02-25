from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
for i in range(3,11):
    tim.color(random.choice(colours))
    for x in range(i):

        tim.forward(100)
        tim.right(360/i)
screen = Screen()
screen.exitonclick()