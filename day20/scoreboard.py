from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-10, 280)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score {self.score}", move=False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.score_update()

