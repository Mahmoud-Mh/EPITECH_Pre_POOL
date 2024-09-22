# Task 3.4
# Download a nice background image and save it in the appropriate folder.
# Modify your main.py program to load and display this background image.

import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))

# Load the background image (update the path to your image)
background = pygame.image.load('path/to/your/background/image.jpg')

# Main loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the window is closed
            pygame.quit()
            sys.exit()

    # Blit the background image onto the screen
    screen.blit(background, (0, 0))  # Position the image at the top-left corner
    pygame.display.flip()  # Update the display
