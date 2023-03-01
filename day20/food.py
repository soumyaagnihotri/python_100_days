from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_rand = random.randint(-270, 270)
        y_rand = random.randint(-270, 270)
        self.goto(x_rand, y_rand)
