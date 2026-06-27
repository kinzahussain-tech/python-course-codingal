import pygame
import sys

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))

# Set window title
pygame.display.set_caption("My First Pygame Screen")

# Background color (White)
bg_color = (255, 255, 255)

# Game loop
running = True
while running:

    # Fill the background
    screen.fill(bg_color)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()