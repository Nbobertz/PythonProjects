from turtle import Turtle


class Turtle_Writes_State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')

    def write_state_on_map(self):
        from main import working_state_ycor, working_state_xcor, lower_user_answer
        self.working_state_xcor = working_state_xcor
        self.working_state_ycor = working_state_ycor
        self.lower_answer = lower_user_answer
        self.goto(self.working_state_xcor,self.working_state_ycor)
        self.write(self.lower_answer, font=('Courier', 8, 'normal'))
        self.goto(0,0)



