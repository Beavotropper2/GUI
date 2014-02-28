
from tkinter import *

class Restaurant(Toplevel):
    
    hotdogPicked = False
    burgerPicked = False
    subPicked = False
    gcheesePicked = False
    friesPicked = False
    potatoPicked = False
    saladPicked = False
    chickenPicked = False
    steakPicked = False

    def __init__(self, original):
        self.original = original
        Toplevel.__init__(self)
        self.title("Restaurant Menu")
        self.grid()
        
        self.makeItems()
        self.makeExitButton()
        
    def makeItems(self):
        self.menuItems = {'hotdog': 1.00, 'burger' : 2.00, 'sub' : 3.00, 'grilled cheese' : 1.50, 
                     'fries' : 1.00, 'potato' : 0.75, 'salad' : 3.50, 'chicken' : 2.50,
                     'steak' : 6.50}
        itemChoices = [self.hotdogPicked, self.burgerPicked, self.subPicked, self.gcheesePicked,
                            self.friesPicked, self.potatoPicked, self.saladPicked, self.chickenPicked,
                            self.steakPicked]
        
        # create menu info
        info = Label(self, justify=CENTER, text="Please select the items you want to purchase")
        info.grid(row=0, column=0, columnspan=2, sticky=N)
        
        # create order check buttons
        index = 0
        row = 1
        for item in self.menuItems.keys():
            text = item + " ${:.2f}".format(self.menuItems[item])
            Checkbutton(self, text=text, variable=itemChoices[index]).grid(row=row, column=0, sticky=W)
            row += 1
            index += 1
            
        # create checkout button
        Button(self, justify=CENTER, text="Get Total Cost", command=self.getTotal).grid()
        
        # create total field
        self.total = Text(self, height=1).grid()
        
    def getTotal(self):
        # calculate total
        totalCost = 0
        for item in self.itemChoices.keys():
            if self.itemChoices[item].get():
                totalCost += self.menuItems[item]

        print(totalCost)
        # display total
        self.total.delete(0.0, END)
        self.total.insert(0.0, str(totalCost))
    
    def makeExitButton(self):
        Button(self, justify=CENTER, text="Exit", command=self.exit).grid()
        
    def exit(self):
        self.destroy()
        self.original.show()