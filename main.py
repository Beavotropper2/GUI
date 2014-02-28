# Added menu to select which gui to run
# GUIs: madlib and restaurant
# Restaurant currently does not calculate toal correctly


from tkinter import *
from menu import Menu

if __name__ == '__main__':
    window = Tk()
    window.title("Simple GUIs")
    app = Menu(window)
    window.mainloop()