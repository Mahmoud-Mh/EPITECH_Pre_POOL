# Task 2.1
# Find the turtle package and install it on your machine.
# This program uses the turtle graphics library to draw a square.

import turtle

def draw_square():
    """Draw a square using turtle graphics."""
    for _ in range(4):
        turtle.forward(100)  # Move forward 100 units
        turtle.right(90)     # Turn right 90 degrees to create a corner

# Call the function to draw a square
draw_square()
turtle.done()  # Finish the drawing
