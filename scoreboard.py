from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.setposition(0, 275)

    def increment_score(self):
        self.score += 1

    def update(self, new_score):
        self.clear()
        self.write(f"Score: {self.score}", False, align='center', font=('Arial', 15, 'normal'))

    def game_over(self):
        self.setposition((0, 0))
        self.write("GAME OVER", False, align='center', font=('Arial', 20, 'normal') )

