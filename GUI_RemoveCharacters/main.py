import tkinter

#below initializes the window
window = tkinter.Tk()
window_2 = tkinter

#names and static size
window.title("Automatic Character Remover For Pacs Entry + Caps Lock")
window.minsize(width=800,height=800)


#label of creator
name_creator = window_2.Label(text="Made by Nick Bobertz", font=("Arial", 12, 'bold'))
name_creator.pack(side='top')


#this stores the string variables from the input and output box
input_var=window_2.StringVar()
output_var=window_2.StringVar()


#Below is label for input directions
direction_l = window_2.Label(text="Input you text to remove characters here", font=("Arial", 18, 'bold')).place(x=10,y=19)

#Below this is the input box for the text to have remove characters
text_input_area = window_2.Entry(width=120,borderwidth=2, textvariable=input_var).place(x=30,y=50)


#This is the output box for text
output_l = window_2.Label(text="Here is your output text after you click submit",font=("Arial", 18, 'bold')).place(x=10,y=70)

#this is the box the text will be pushed to
text = window_2.Text()
text.config(font=('courier',10,'normal'))
text.config(width=65,height=20)
text.place(x=10,y=100)


#This code to replace the characters in the string when it get's called by the button.
banned_characters = '!@#$%^&*'
new_str = ""
correct_str=''
def logic():
    #this is to test that the function is called and text is pulled from input window print(input_var.get())
    str_input = input_var.get()
    str_u_input = str_input.upper()
    correct_str = ''
    print(str_u_input)
    for n in str_u_input:
        if n not in banned_characters:
            correct_str += n
        else:
            pass
    print(correct_str)
    text.insert('1.0',correct_str)


#This is the output entry log for copying into PACS

#below is the code for the button
submit_button = window_2.Button(text="Submit for Refactor",command=logic).place(x=500,y=550)
#end code block

#this is the logic for the conversion of the txt input











window.mainloop()

