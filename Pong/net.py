from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.teleport(0, 300)
        self.pensize(5)
        self.dotted_line()

    def dotted_line(self):
        while self.ycor() > -300:
            self.setheading(270)
            self.forward(25)
            self.penup()
            self.forward(40)
            self.pendown()

