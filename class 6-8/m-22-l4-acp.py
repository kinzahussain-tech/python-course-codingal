import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Custom Event Example")

# Background color
WHITE = (255, 255, 255)

# Create two rectangle sprites
sprite1 = pygame.Rect(150, 200, 100, 100)
sprite2 = pygame.Rect(500, 200, 100, 100)

# Initial colors
color1 = (255, 0, 0)      # Red
color2 = (0, 0, 255)      # Blue

# Create a custom event
CHANGE_COLOR = pygame.USEREVENT + 1

# Trigger the custom event every 2000 milliseconds (2 seconds)
pygame.time.set_timer(CHANGE_COLOR, 2000)

# Game loop
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Custom event to change colors
        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # Fill background
    screen.fill(WHITE)

    # Draw sprites
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()