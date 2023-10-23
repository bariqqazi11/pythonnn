#pygame project

import pygame

# initializing python
pygame.init()

w = 1000
h = 800

# defining screen
screen = pygame.display.set_mode((w, h))

# setting title and icon
pygame.display.set_caption("Space Invaders")
logo = pygame.image.load("ufooo.png")
pygame.display.set_icon(logo)

# game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False
