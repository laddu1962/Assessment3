import pygame
import random

screen_width = 1200
screen_height = 700
FPS = 60

pygame.init()
# mixer is for the sounds of the game
pygame.mixer.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # updates

    # draw
    screen.fill('grey')
    # flipping the display?
    pygame.display.flip()

pygame.quit()