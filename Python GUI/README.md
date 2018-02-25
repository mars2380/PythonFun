### Python GUI Examples (Tkinter Tutorial)

In this tutorial, we will learn how to develop graphical user interfaces by writing some Python GUI examples using Tkinter package.
Tkinter package is shipped with Python as a standard package, so we don’t need to install anything to use it.
Tkinter package is a very powerful package. If you already have installed Python, you may use IDLE which is the integrated IDE that is shipped with Python, this IDE is written using Tkinter. Sounds Cool!!
We will use Python 3.6, so if you are using Python 2.x, it’s strongly recommended to switch to Python 3.x unless you know the language changes so you can adjust the code to run without errors.
I assume that you a little background about Python basics to help you understand what we are doing.
We will start by creating a window then we will learn how to add widgets such as buttons, combo boxes, etc, then we will play with their properties, so let’s get started.

### Create your first GUI application

First, we will import Tkinter package and create a window and set its title:

    from tkinter import *
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.mainloop()

The last line which calls mainloop function, this function calls the endless loop of the window, so the window will wait for any user interaction till we close it.
If you forget to call the mainloop function, nothing will appear to the user.

### Create a label widget
To add a label to our previous example, we will create a label using the label class like this:

    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)

    from tkinter import *
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)
    window.mainloop()

Without calling the grid function for the label, it won’t show up.