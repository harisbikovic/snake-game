from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
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
        self.score = 0
        self.update()

    #def game_over(self):
    #    self.setposition((0, 0))
    #    self.write("GAME OVER", False, align='center', font=('Arial', 20, 'normal') )

