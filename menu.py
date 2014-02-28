
from tkinter import *
from madlib import MadLib
from restaurant import Restaurant

class Menu(Frame):

    def __init__(self, parent):
        self.root = parent
        self.root.title("GUI Menu")
        self.frame = Frame(parent)
        self.frame.grid()
        
        self.createChoices()
        
    def createChoices(self):
        Label(self.frame, justify=CENTER, text="Welcome to the simple GUIs program").grid(row=0)
        Label(self.frame, justify=CENTER, text="Select a GUI to run").grid(row=1)
        
        self.madLibButton = Button(self.frame, text="Go to Mad Lib GUI", command=self.goToMadLib)
        self.madLibButton.grid(row=2)
        self.restaurantButton = Button(self.frame, text="Go to restaurant GUI", command=self.goToRestaurant)
        self.restaurantButton.grid(row=3)
        self.exitButton = Button(self.frame, text="Exit", command=self.exit)
        self.exitButton.grid(row=4)
        
    def exit(self):
        self.root.destroy()
        
    def goToMadLib(self):
        self.root.withdraw()
        madlib = MadLib(self)
    
    def goToRestaurant(self):
        self.root.withdraw()
        restaurant = Restaurant(self)
        
    def show(self):
        self.root.update()
        self.root.deiconify()