import pygame

pygame.init()
# Create the display surface object of specific dimension.
window = pygame.display.set_mode((400, 400))
# Fill the screen with white color
window.fill((255, 255, 255))
# Define colors
BLUE = (0, 0, 255)
# Draw solid circle
pygame.draw.circle(window, BLUE, (300, 300), 50)
# Draw outlined circle
pygame.draw.circle(window, BLUE, (100, 100), 50, 3)
# Draws the surface object to the screen.
pygame.display.update()
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quit pygame
pygame.quit()