from turtle import Turtle

ALLIGNMENT = "center"
FONT_1 = ("Arial",20,"normal")
FONT_2 = ("Arial",40,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.print_score()

    def print_score(self):
        self.write(f"Score : {self.score}", align=ALLIGNMENT, font=FONT_1)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALLIGNMENT, font=FONT_2)
        self.goto(0,-50)
        self.print_score()

