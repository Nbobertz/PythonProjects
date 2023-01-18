from turtle import Turtle, Screen

#this code block starts the Screen and Turtle files

screen = Screen()
turtle = Turtle()
#end code block

#this code block sets up the screen
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title("The 3 Rings")

#this code block creates the turtle and has it draw
turtle.color('black')
turtle.pendown()
turtle.speed(.5)
#function for how many turns to have
amount_of_turns = 100
turtle.goto(0,0)


# I do not use for loops because this file is used for training people on how to do for loops: NB


#start of circles
for amount in range(0,amount_of_turns):
    turtle.forward(10)
    turtle.right(amount_of_turns/2)
    turtle.forward(15)
    turtle.right(amount_of_turns/5)
    turtle.forward(30)
    turtle.right(amount_of_turns / 10)
    turtle.forward(60)
    turtle.right(amount_of_turns / 20)
#end of code block
turtle.penup()
turtle.goto(30,0)
turtle.pendown()
for amount in range(0,amount_of_turns):
    turtle.forward(10)
    turtle.right(amount_of_turns/2)
    turtle.forward(15)
    turtle.right(amount_of_turns/5)
    turtle.forward(30)
    turtle.right(amount_of_turns / 10)
    turtle.forward(60)
    turtle.right(amount_of_turns / 20)
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
for amount in range(0,amount_of_turns):
    turtle.forward(10)
    turtle.right(amount_of_turns/2)
    turtle.forward(15)
    turtle.right(amount_of_turns/5)
    turtle.forward(30)
    turtle.right(amount_of_turns / 10)
    turtle.forward(60)
    turtle.right(amount_of_turns / 20)




screen.exitonclick()