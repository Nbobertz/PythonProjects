import tkinter

#below initializes the window
window = tkinter.Tk()



#names and static size
window.title('First GUI Program')
window.minsize(width=500,height=300)

#label
label =tkinter.Label(text="I am a label", font=("Arial", 24, 'bold'))
label.pack(expand=True)











window.mainloop()

