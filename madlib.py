
from tkinter import *

class MadLib(Toplevel):

    def __init__(self, original):
        self.original = original
        Toplevel.__init__(self)
        self.title("Mad Lib")
        self.grid()
        
        self.makeLabels()
        self.makeCheckButtons()
        self.makeEntries()
        self.makeRadioButtons()
        self.makeButton()
        self.makeStoryPanel()
        self.makeExitButton()
        
    def genStory(self):
        # get values from the GUI
        person = self.personEntry.get()
        noun = self.plrlNounEntry.get()
        verb = self.verbEntry.get()
        adjectives = ""
        if self.isItchy.get():
            adjectives += "itchy, "
        if self.isJoyous.get():
            adjectives += "joyous, "
        if self.isElectric.get():
            adjectives += "electric, "
        bodyPart = self.bodyPart.get()
        
        # create the story
        story = "The famous explorer "
        story += person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + ". "
        story += "A strong, "
        story += adjectives
        story += "peculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += bodyPart + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."

        # display the story
        self.storyPanel.delete(0.0, END)
        self.storyPanel.insert(0.0, story)
        
    def makeLabels(self):
        instrLabel = Label(self, text="Enter information for a new story")
        instrLabel.grid(row=0, column=0, columnspan=2, sticky=W)
        
        personLabel = Label(self, text="Person:")
        personLabel.grid(row=1, column=0, sticky=W)
        
        plrlNounLabel = Label(self, text="Plural Noun:")
        plrlNounLabel.grid(row=2, column=0, sticky=W)
        
        verbLabel = Label(self, text="Verb:")
        verbLabel.grid(row=3, column=0, sticky=W)
        
        adjLabel = Label(self, text="Adjective(s):")
        adjLabel.grid(row=4, column=0, sticky=W)
        
        bdyPartLabel = Label(self, text="Body Part:")
        bdyPartLabel.grid(row=5, column=0, sticky=W)
        
    def makeEntries(self):
        self.personEntry = Entry(self)
        self.personEntry.grid(row=1, column=1, sticky=W)
        
        self.plrlNounEntry = Entry(self)
        self.plrlNounEntry.grid(row=2, column=1, sticky=W)
        
        self.verbEntry = Entry(self)
        self.verbEntry.grid(row=3, column=1, sticky=W)
        
    def makeCheckButtons(self):
        self.isElectric = BooleanVar()
        self.isItchy = BooleanVar()
        self.isJoyous = BooleanVar()
        
        itchyCheckButton = Checkbutton(self, text="itchy", variable=self.isItchy)
        itchyCheckButton.grid(row=4, column=1, sticky=W)
        
        joyousCheckButton = Checkbutton(self, text="joyous", variable=self.isJoyous)
        joyousCheckButton.grid(row=4, column=2, sticky=W)
        
        electricCheckButton = Checkbutton(self, text="electric", variable=self.isElectric)
        electricCheckButton.grid(row=4, column=3, sticky=W)
        
    def makeRadioButtons(self):
        self.bodyPart = StringVar()
        self.bodyPart.set(None)
        
        # create radio buttons
        bodyParts = ["bellybutton", "big toe", "medulla oblongata"]
        column = 1
        for part in bodyParts:
            Radiobutton(self, text=part, variable=self.bodyPart, value=part).grid(row=5, column=column, sticky=W)
            column += 1
        
    def makeButton(self):
        genStoryButton = Button(self, text="Click for story", command=self.genStory)
        genStoryButton.grid(row=6, column=0, sticky=W)
        
    def makeStoryPanel(self):
        self.storyPanel = Text(self, width=75, height=10, wrap=WORD)
        self.storyPanel.grid(row=7, column=0, columnspan=4)
        
    def makeExitButton(self):
        Button(self, justify=CENTER, text="Exit", command=self.exit).grid(row=8, column=0, sticky=S)
        
    def exit(self):
        self.destroy()
        self.original.show()
    