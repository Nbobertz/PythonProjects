import random
from turtle import Turtle, Screen
import random as rr

#global
screen = Screen()
turt = Turtle()
heading = 90
num_of_squares = input('How many squares would you like?')
int_num_of_squares = int(num_of_squares)
turt.speed(8)


#this itemizes the turtle and sets it facing north. Pen color is black.
screen.screensize(700,700, 'white')
turt.pencolor('black')
turt.goto(0,0)
turt.setheading(90)



#This is the function for a square
def square():
    turt.forward(20)
    turt.right(90)
    turt.forward(20)
    turt.right(90)
    turt.forward(20)
    turt.right(90)
    turt.forward(20)
    turt.right(90)


def change_heading():
    for n in range(0,int_num_of_squares):
        heading1 = heading + (n*10)
        turt.setheading(heading1)
        square()

def another_one():
    heading2=random.randint(0,360)
    turt.setheading(heading2)
    turt.forward(60)

def number_of_squares():
    for n in range(0,int_num_of_squares):
        change_heading()
        another_one()

number_of_squares()

#thisis the number of squares












#this allows the screen to exit on click
screen.exitonclick()