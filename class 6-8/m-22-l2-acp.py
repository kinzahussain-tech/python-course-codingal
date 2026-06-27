import pygame
import sys

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 40)

# Create text
text = font.render("Welcome to Pygame!", True, BLACK)

# Game loop
running = True
while running:

    # Fill background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (250, 200, 300, 150))

    # Display text
    screen.blit(text, (230, 100))

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()