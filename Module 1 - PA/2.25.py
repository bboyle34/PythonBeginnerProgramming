#Client name: Professor Laura Atkins
#Programmer name: Brendan Boyle
#PA Purpose: The program prompts the user to enter a center point, a width, and a height and then uses turtle to create a rectangle according to those coordinates.
# My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.

centerX,centerY = eval(input("Enter the coordinates for the center of your rectangle separated by a comma:"))
width = eval(input("Enter the width of your rectangle:"))
height = eval(input("Enter the height of your rectangle:"))

import turtle

turtle.penup()
turtle.goto(centerX,centerY)
turtle.goto(width/2,centerY)
turtle.pendown()
turtle.left(90)
turtle.forward(height/2)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)

turtle.done()
