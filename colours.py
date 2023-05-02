from tkinter import *
import random
window = Tk()

window.title("Colours")
window.geometry("600x400")


dic1 = {

"Colours":["DodgerBlue2","lawn green","brown1","gold","dark orchid","hot pink","orange"]

}

def bg_change():
    x = random.randint(0,6)
    window.configure(background=dic1["Colours"][x])


btn1 = Button(window,text="Click me!",command=bg_change)


btn1.place(relx=0.5,rely=0.5,anchor=CENTER)

window.mainloop()