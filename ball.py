from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.setposition(0, 0)
        self.penup()
        self.color("white")
        self.yspeed = 10
        self.xspeed = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.xspeed, self.ycor() + self.yspeed)

    def bounce_from_wall(self):
        self.yspeed *= -1

    def bounce_from_paddle(self):
        self.xspeed *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.setposition(0, 0)
        self.bounce_from_paddle()
