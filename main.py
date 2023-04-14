import pygame
from pygame.locals import *
import random


screen_width = 1200
screen_height = 700
FPS = 60

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

bg_img = pygame.image.load('graphics/bg1.jpg')

tile_size = 32


def draw_grid():
    for line in range(0,40):
        pygame.draw.line(screen, (255,255,255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255,255,255), (line * tile_size, 0), (line * tile_size, screen_height))


class World():
    def __int__(self, data):
        self.tile_list = []

        dirt_img = pygame.image.load('graphics/Tile.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


world_data = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    ]

world = World(world_data)

run = True
while run:
    clock.tick(FPS)

    screen.blit(bg_img, (0, 0))

    #world.draw()

    draw_grid()

    print(world.tile_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # flipping the display?
    pygame.display.update()

pygame.quit()