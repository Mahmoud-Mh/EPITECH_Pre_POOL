# Task 2.4
# This program uses the turtle library to draw a spiral.

import turtle

def draw_spiral():
    """Draw a spiral using turtle graphics."""
    for i in range(100):
        turtle.forward(i * 10)  # Move forward increasing distance
        turtle.right(144)       # Turn right 144 degrees

draw_spiral()
turtle.done()  # Finish the drawing
