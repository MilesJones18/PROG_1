import turtle


def create_star():
    size = 200  # Defines the length of each side.

    turtle.color('black')  # Pen color and width.
    turtle.width(4)


    angle = 140  # Defines the angle that of each point.

    
    turtle.penup()  # Goes to a point that I found where the center of the star will be (0,0).
    turtle.goto(60, 100)
    turtle.pendown()


    for side in range(5):  # Creates the star.
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72-angle)

    turtle.penup() # Goes to (0,0).
    turtle.home()
    turtle.pendown()

    turtle.write('Miles Jones', align='center', font=('Arial', 30, 'normal'))  # Writes my name.


if __name__ == '__main__':
    screen = turtle.Screen()
    canvas = screen.getcanvas()
    canvas.create_window(-200, -200,window=create_star())
    turtle.done()
    