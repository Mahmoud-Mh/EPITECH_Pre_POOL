# Task 3.2
# Create a main.py program in your hangman folder.
# This program initializes Pygame and sets up a window.

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window with a width and height of 600 pixels
screen = pygame.display.set_mode((600, 600))

# Briefly show the window
pygame.display.flip()  # Update the display
pygame.time.delay(2000)  # Delay for 2 seconds to view the window

pygame.quit()  # Close Pygame
sys.exit()     # Exit the program
