import turtle
import pandas as pd
from turtle_writes_state import Turtle_Writes_State

#this creates the screen we will host the game on and then makes it he U.S map: NB
screen = turtle.Screen()
screen.title('Nicks U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
#end code block

#this block of code imports Pandas and reads the CSV file into a variable
data = pd.read_csv('50_states.csv')
#end of code block

#This code block seperates the following colums into 3 lists; state, x, and y
state = data['state'].tolist()
x_cor = data['x'].tolist()
y_cor = data['y'].tolist()
#end of code block

#this code block tests to make sure the lists lighn up so we can call them
# print(state[1])
# print(x_cor[1])
# print(y_cor[1])
#end of code block

#this makes all entries in state list lowercase
working_state_list = []
open_var = ''
for n in range(0,len(state)):
    open_var = state[n]
    open_var=open_var.lower()
    state[n] = open_var
#end code block

#this initalises the writer py file so we dont get an error.
writer = Turtle_Writes_State()
#end code block

#this code block makes secondary lists we will delete from as user gets correct answer\
working_state_list = state
working_x_cor = x_cor
working_y_cor = y_cor
#end of code block

#this code block contains the logic for the game
end_of_game = False
while end_of_game == False:
    user_answer_raw = screen.textinput(title="Guess the State!",prompt="Guess another state's name and I will mark it on the map.")
    lower_user_answer = user_answer_raw.lower()
    #this code block checks to see if the user answer is in the state list and then send the name to the map
    if lower_user_answer in working_state_list:
        index_pos = state.index(lower_user_answer)
        working_state_xcor = working_x_cor[index_pos]
        working_state_ycor = working_y_cor[index_pos]
        print(working_state_xcor)
        print(working_state_ycor)
        writer.write_state_on_map()

        #after we get the name on the map we remove it and the cor's from their lists
        working_x_cor.remove(working_state_xcor)
        working_y_cor.remove(working_state_ycor)
        working_state_list.remove(lower_user_answer)
    else:
        pass

# #At the end of the game this will close it down by calling exit on click
# screen.exitonclick()
