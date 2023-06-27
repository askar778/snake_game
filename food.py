from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        self.x = randint(-280, 280)
        self.y = randint(-280, 280)
        super().goto(self.x, self.y)

    #code to make the food blink
    # def blink(self):
    #     for x in range (100):
    #         self.shapesize(0.5,0.5)
    #         self.color("blue")
    #         self.shapesize(0.1, 0.1)
    #         self.color("white")



