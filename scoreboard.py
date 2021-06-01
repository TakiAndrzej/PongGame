from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.setposition(position)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.write_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
