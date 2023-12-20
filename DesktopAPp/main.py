import tkinter
from tkinter import  *

def get_input():
    user_input = textbox.get()  # Retrieve the text entered in the Entry widget
    # print("User input:", user_input)
    text2.config(text="User input: " + user_input)


window= tkinter.Tk()
window.geometry("860x500")
window.title("Jivesh")
bg_color= "#0077be"
window.configure(bg=bg_color)

text1=Label (window, text= "Hello", background=bg_color, foreground="black",font=("Arial", 20))
text1.grid (column=1, row=1)

text2=Label (window, text= "", background=bg_color, foreground="black",font=("Arial", 20))
text2.grid (column=1, row=7)

textbox= Entry (window)
textbox.grid (column=5, row=1)


# Create a button to capture the input
button = Button(window, text="Get Input", command=get_input)
button.grid (column=5, row=4)


window.mainloop()