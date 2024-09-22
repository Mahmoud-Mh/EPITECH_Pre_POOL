# Task 3.5
# Create a function to draw a stickman inside the game window.

import pygame
import sys

def draw_stickman(screen, x, y):
    """Draw a stickman at the specified coordinates (x, y)."""
    # Head
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 10)  # Draw the head
    # Body
    pygame.draw.line(screen, (0, 0, 0), (x, y + 10), (x, y + 50), 2)  # Draw the body
    # Arms
    pygame.draw.line(screen, (0, 0, 0), (x - 15, y + 20), (x + 15, y + 20), 2)  # Draw arms
    # Legs
    pygame.draw.line(screen, (0, 0, 0), (x, y + 50), (x - 15, y + 80), 2)  # Draw left leg
    pygame.draw.line(screen, (0, 0, 0), (x, y + 50), (x + 15, y + 80), 2)  # Draw right leg

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))

# Main loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the window is closed
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # Clear the screen with white
    draw_stickman(screen, 300, 100)  # Draw stickman at specified coordinates
    pygame.display.flip()  # Update the display
