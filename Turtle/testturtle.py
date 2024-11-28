import turtle
import time
import colorsys  # For generating rainbow colors

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Setup turtle
myTurtle = turtle.Turtle()
myTurtle.speed(0)
myTurtle.width(2)

# Rainbow effect
for i in range(36):  # Outer loop for rotating the star pattern
    # Generate a color from the HSV spectrum (hue cycles through 0 to 1)
    hue = i / 36  # Divide by 36 to get evenly spaced colors
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
    myTurtle.color(r, g, b)  # Set turtle color using RGB

    for j in range(5):  # Inner loop for drawing a star
        myTurtle.forward(100)
        myTurtle.right(144)
    myTurtle.right(10)  # Rotate the turtle slightly for the next star

# Keep the window open
screen.mainloop()
