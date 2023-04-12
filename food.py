from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # 10 by 10 circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # We don't use 300 since it'd be
        random_y = random.randint(-280, 280)  # hard to catch food at the edge of screen
        self.goto(random_x, random_y)
