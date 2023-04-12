import pygame
import sys
from sys import exit

screen_width = 1200
screen_height = 700

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')


    pygame.display.update()
    clock.tick(60)



