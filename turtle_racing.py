import turtle 
import random
import tkinter as tk

import time

WIDTH , HEIGHT = 500, 500
COLORS = ['red','green', 'blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers():
    racers=0
    while True:
        racers = input('Enter the number of racers (2- 10): ')
        if racers.isdigit():
            racers= int(racers)
        else:
            print('Input is not numeric...Try Again!')
            continue
    
        if 2 <= racers <=10:
            return racers
        else:
            print('Number not in range of 2-10.Then try again!')

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if(y) >= HEIGHT //2 -10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles = []
    spacingx= WIDTH // (len(colors)+1)
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i + 1)*spacingx, -HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def init_turtle():
    screen = turtle.Screen()
    rootwindow = screen.getcanvas().winfo_toplevel()
    # Bring the window to the front using Tkinter's lift method
    rootwindow.attributes('-topmost', True)
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')


racers= get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors=COLORS[:racers]

winner= race(colors)
print("The winner is the turtle with color:",winner)