
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('500x300')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=1)

def clicked():

    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
#   lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=1)

combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=3)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=4)

rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=5)
rad2.grid(column=1, row=5)
rad3.grid(column=2, row=5)

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column=0,row=6)

window.mainloop()