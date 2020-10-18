import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random


# Create the window with the Tk class
root = Tk()
root.geometry("1550x850")

# Define variables for dimensions
w = 1145
h = 800
x = w/2
y = h/2

# Create the canvas and make it visible with pack()
canvas = Canvas(root, width=1145, height=800)
canvas.place(x=200, y=200)
canvas.pack()  # this makes it visible

# Define list of images for dice
dice1 = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
dice2 = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']


# Create class of stone type
class Stone():

    def __init__(self, x, y, rangex, rangey, rangezx, rangezy, color):

        super().__init__()
        self.x = x
        self.y = y
        self.rangex = rangex
        self.rangey = rangey
        self.rangezx = rangezx
        self.rangezy = rangezy
        self.color = color

    def b_create(self):
        self.img = PhotoImage(
            file="C:/Users/edens/Desktop/GitHub Projects/Python Projects/Backgammon/images/brown_stone.png")
        img3 = canvas.create_image(self.x, self.y, image=self.img)
        return

    def w_create(self):
        self.img = PhotoImage(
            file="C:/Users/edens/Desktop/GitHub Projects/Python Projects/Backgammon/images/white_stone.png")
        img3 = canvas.create_image(self.x, self.y, image=self.img)
        return

    def get_posrangex(self):
        return self.rangex

    def get_posrangey(self):
        return self.rangey

    def get_posrangezx(self):
        return self.rangezx

    def get_posrangezy(self):
        return self.rangezy

    def get_color(self):
        return self.color


# Load the images of dice
DiceImage1 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
DiceImage2 = ImageTk.PhotoImage(Image.open(random.choice(dice2)))


# Construct a label widget for image
ImageLabel1 = tk.Label(root, image=DiceImage1)
ImageLabel1.image = DiceImage1
ImageLabel2 = tk.Label(root, image=DiceImage2)
ImageLabel2.image = DiceImage2


# Place the images in specific position
ImageLabel1.place(x=50, y=70)
ImageLabel2.place(x=50, y=200)


# Loads and create image of the game board
img1 = tk.PhotoImage(file="board.jpg")
image = canvas.create_image(0, 0, anchor=tk.NW, image=img1)

# Create the stones in the starting position
B_List = [Stone(655, 50, 655+32, 50+32, 655-32, 50-32, "brown"),
          Stone(655, 115, 655+32, 115+32, 655-32, 115-32, "brown"),
          Stone(655, 180, 655+32, 180+32, 655-32, 180-32, "brown"),
          Stone(655, 245, 655+32, 245+32, 655-32, 245-32, "brown"),
          Stone(655, 310, 655+32, 310+32, 655-32, 310-32, "brown"),

          Stone(400, 50, 400+32, 50+32, 400-32, 50-32, "brown"),
          Stone(400, 115, 400+32, 115+32, 400-32, 115-32, "brown"),
          Stone(400, 180, 400+32, 180+32, 400-32, 180-32, "brown"),

          Stone(57, 750, 57+32, 750+32, 57-32, 750-32, "brown"),
          Stone(57, 685, 57+32, 685+32, 57-32, 685-32, "brown"),
          Stone(57, 620, 57+32, 620+32, 57-32, 620-32, "brown"),
          Stone(57, 555, 57+32, 555+32, 57-32, 555-32, "brown"),
          Stone(57, 490, 57+32, 490+32, 57-32, 490-32, "brown"),

          Stone(1088, 750, 1088+32, 750+32, 1088-32, 750-32, "brown"),
          Stone(1088, 685, 1088+32, 685+32, 1088-32, 685-32, "brown"),

          Stone(655, 750, 655+32, 750+32, 655-32, 750-32, "white"),
          Stone(655, 685, 655 + 32, 685 + 32, 655 - 32, 685 - 32, "white"),
          Stone(655, 620, 655 + 32, 620 + 32, 655 - 32, 620 - 32, "white"),
          Stone(655, 555, 655 + 32, 555 + 32, 655 - 32, 555 - 32, "white"),
          Stone(655, 490, 655 + 32, 490 + 32, 655 - 32, 490 - 32, "white"),

          Stone(400, 750, 400+32, 750+32, 400-32, 750-32, "white"),
          Stone(400, 685, 400+32, 685+32, 400-32, 685-32, "white"),
          Stone(400, 620, 400+32, 620+32, 400-32, 620-32, "white"),

          Stone(57, 50, 57+32, 50+32, 57-32, 50-32, "white"),
          Stone(57, 115, 57+32, 115+32, 57-32, 115-32, "white"),
          Stone(57, 180, 57+32, 180+32, 57-32, 180-32, "white"),
          Stone(57, 245, 57+32, 245+32, 57-32, 245-32, "white"),
          Stone(57, 310, 57+32, 310+32, 57-32, 310-32, "white"),

          Stone(1088, 50, 1088+32, 50+32, 1088-32, 50-32, "white"),
          Stone(1088, 115, 1088+32, 115+32, 1088-32, 115-32, "white"),

          Stone(1600, 1600, 1600+65, 1600+65, 0, 0, "red")]


# Put the stones in game board (by slicing-brown stones 0-15, white stones 15-31)
for obj in B_List[0:15]:
    obj.b_create()

for obj in B_List[15:31]:
    obj.w_create()


# Function to rolling the dice (function activated by button)
def rolling_dice():

    # Randomize the dice and load the choice
    choice1 = random.choice(dice1)
    DiceImage1 = ImageTk.PhotoImage(Image.open(choice1))
    choice2 = random.choice(dice2)
    DiceImage2 = ImageTk.PhotoImage(Image.open(choice2))

    # update image
    ImageLabel1.configure(image=DiceImage1)
    ImageLabel2.configure(image=DiceImage2)

    # keep a reference
    ImageLabel1.image = DiceImage1
    ImageLabel2.image = DiceImage2


# Define the global variables of the coordinates
xclick = 0
yclick = 0

# Define global variable to hold the index of specific stone
p = 0


# Function to hold the image updated when the mouse in move
def move(event):

    global xclick
    global yclick
    global t
    global r

    if (p != None) and (B_List[p].get_color() == "brown"): # p cannot contains None
     t = PhotoImage(file="C:/Users/edens/Desktop/GitHub Projects/Python Projects/Backgammon/images/brown_stone.png")
     image1 = canvas.create_image(event.x, event.y, image=t)
     for obj in B_List[0:15]: # Refresh the stones after the move event
        obj.b_create()

    if (p != None) and (B_List[p].get_color() == "white"):
      r = PhotoImage(file="C:/Users/edens/Desktop/GitHub Projects/Python Projects/Backgammon/images/white_stone.png")
      image11 = canvas.create_image(event.x, event.y, image=r)
      for obj in B_List[15:31]:
        obj.w_create()


# Function to save the coordinates after the click
def click(event):

    global p
    global xclick
    global yclick
    xclick = event.x
    yclick = event.y

    print(xclick, yclick) # Status of the coordinates after click

    # Checking which stone it is
    p = isstone(xclick, yclick)

    print(p) # The list number of the stone

    # Remove the stone from the canvas after click
    if (p != None) and (B_List[p].get_color() == "brown"):
        B_List[p] = Stone(1600, 1600, 0, 0, 0, 0,"brown")
    elif (p != None) and (B_List[p].get_color() == "white"):
        B_List[p] = Stone(1600, 1600, 0, 0, 0, 0, "white")


# Function to save the coordinates after release the click
def release(event):

        global p
        global xclick
        global yclick
        xclick = event.x
        yclick = event.y

        # Update the new coordinates after release
        if (p != None) and (B_List[p].get_color() == "brown"):
         B_List[p] = Stone(xclick, yclick, xclick + 32, yclick + 32, xclick - 32, yclick - 32,"brown")
        elif (p != None) and (B_List[p].get_color() == "white"):
         B_List[p] = Stone(xclick, yclick, xclick + 32, yclick + 32, xclick - 32, yclick - 32, "white")


# Function to check if the coordinates after the click is belong to the stones or game board
def isstone(xz, yz):
    i = 0
    while i < len(B_List):
        if (B_List[i].get_posrangezx() <= xz) and (B_List[i].get_posrangex() >= xz) and (B_List[i].get_posrangezy() <= yz) and (B_List[i].get_posrangey() >= yz):
            return i
        else:
            i += 1


# This bind window to keys so that move is called when you press a key
canvas.bind('<Button-1>', click)
canvas.bind('<B1-Motion>', move)
canvas.bind('<ButtonRelease-1>', release)


# adding button, and command will use rolling_dice function
button = tk.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.place(x=60, y=350)


# this creates the loop that makes the window stay 'active'
root.mainloop()
