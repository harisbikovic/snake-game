from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.get_high_score())
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.setposition(0, 275)

    def increment_score(self):
        self.score += 1

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align='center', font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_high_score()
        self.score = 0
        self.update()

    def get_high_score(self):
        with open("high_score.txt") as file:
            return file.read()

    def write_new_high_score(self):
        with open("high_score.txt", mode = "w") as file:
            file.write(str(self.high_score))

