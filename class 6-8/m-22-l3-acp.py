import pygame
import sys

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rectangle Sprite Movement")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player rectangle (movable)
player = pygame.Rect(100, 100, 80, 60)

# Enemy rectangle (fixed)
enemy = pygame.Rect(500, 300, 80, 60)

# Speed
speed = 2

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check pressed keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Fill background
    screen.fill(WHITE)

    # Draw rectangles
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()