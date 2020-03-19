
import turtle

# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Write a text at the specified location (x, y)
def writeText(s, x, y): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.write(s) # Write a string

# Draw a point at the specified location (x, y)
def drawPoint(x, y): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.begin_fill() # Begin to fill color in a shape
    turtle.circle(3) 
    turtle.end_fill() # Fill the shape

# Draw a circle at centered at (x, y) with the specified radius
def drawCircle(x, y, radius): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y - radius)
    turtle.pendown() # Pull the pen down
    turtle.circle(radius) 
    
# Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x, y, width, height): 
    turtle.penup() # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)

def menu():
    print("Your options: \n(l)ine \n(t)ext - \n(p)oint - \n(c)ircle - \n(r)ectangle")
    choice = input("Choose one of the following: ")
    main()
def main():
    menu()
    if choice[0].upper() == "L":
        drawLine()
    elif choice[0].upper() == "T":
        writeText()
    elif choice[0].upper() == "P":
        drawPoint()
    elif choice[0].upper() == "C":
        drawCircle()
    elif choice[0].upper() == "R":
        drawRectangle()
    else:
        print("Please enter a valid option.")
        menu()
main()
        
        

