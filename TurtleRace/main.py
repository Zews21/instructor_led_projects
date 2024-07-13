from turtle import Turtle, Screen
import random

racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win the race? Enter a color: ")
y_positions = [-125, -75, -25, 25, 75, 125]
colors = ["green", "blue", "red", "yellow", "orange", "purple"]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    racing = True

while racing:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
