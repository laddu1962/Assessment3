import pygame
from setting import *


class Player(pygame.sprite.Sprite):
    def __int__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((Tile_Size // 2, Tile_Size))
        self.image.fill(Player_colour)
        self.rect = self.image.get_rect(topleft=pos)