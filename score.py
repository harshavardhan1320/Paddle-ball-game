from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 30, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 00
        self.score_2 = 00
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-50, 250)
        self.write(arg=self.score_1, move=False, align=ALIGNMENT, font=FONT)
        self.goto(50, 250)
        self.write(arg=self.score_2, move=False, align=ALIGNMENT, font=FONT)

    def increase_score_1(self):
        self.score_1 += 1
        self.clear()
        self.update_score()
        return True

    def increase_score_2(self):
        self.score_2 += 1
        self.clear()
        self.update_score()
        return True



