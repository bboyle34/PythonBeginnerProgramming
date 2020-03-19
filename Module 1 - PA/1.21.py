#Client name: Professor Laura Atkins
#Programmer name: Brendan Boyle
#PA Purpose: This displays a clock showing 9:15 using turtle.
#My submission of this program indicates that I have neither received nor given substantial assistance in writing this program.

import turtle

turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.circle(200)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.forward(175)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("red")
turtle.left(90)
turtle.forward(175)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("black")
turtle.left(90)
turtle.forward(125)

turtle.penup()
turtle.goto(-15,-220)
turtle.pendown()
turtle.write("9:15:00")
turtle.penup()
turtle.goto(0,-197)
turtle.pendown()
turtle.write(6)
turtle.penup()
turtle.goto(-195,-10)
turtle.pendown()
turtle.write(9)
turtle.penup()
turtle.goto(190,-5)
turtle.pendown()
turtle.write(3)
turtle.penup()
turtle.goto(-5,185)
turtle.pendown()
turtle.write(12)

turtle.done
