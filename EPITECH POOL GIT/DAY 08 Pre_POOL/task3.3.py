# Task 3.3
# Add a loop to keep the Pygame window running and listen for events.

import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))

# Main loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the window is closed
            pygame.quit()
            sys.exit()

    # Optionally, fill the screen with a color (white in this case)
    screen.fill((255, 255, 255))  # Fill with white color
    pygame.display.flip()  # Update the display
