import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1200
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')


tile_size = 64

bg_img = pygame.image.load('graphics/backGround.png')


class Player:
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.images_jump =[]
        self.index = 0
        self.counter = 0
        for num in range(0, 9):
            img_right = pygame.image.load(f'graphics/player0{num}.png')
            img_right = pygame.transform.scale(img_right, (128, 128))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        for num in range(1, 3):
            img_jump = pygame.image.load(f'graphics/jump{num}.png')
            img_jump = pygame.transform.scale(img_jump, (128, 128))
            self.images_jump.append(img_jump)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        jump_cooldwon = 5

        # player movement - keys
        key = pygame.key.get_pressed()
        # player movement (jump)
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = - 15
            self.jumped = True
            self.direction = 2
            self.counter = 0
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        # player movement (left and right)
        if key[pygame.K_a]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_d]:
            dx += 5
            self.counter += 1
            self.direction = 1
        # if the player isn't moving then no animation
        if key[pygame.K_a] == False and key[pygame.K_d] == False:
            self.counter = 0
            self.index = 0
        # when player stops moving they are facing the direction they stopped at
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]

        # animation speed
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index == len(self.images_right):
                self.index = 0
            # animation depending on the direction
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        if self.counter > jump_cooldwon:
            self.counter = 0
            self.index += 1
            if self.direction == 2:
                self.image = self.images_jump[self.index]

        # gravity for the player
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # updates for the player position/ coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        screen.blit(self.image, self.rect)


class World:
    def __init__(self, data):
        self.tile_list = []
        # individual tile images
        dirt_img = pygame.image.load('graphics/Tile.png')
        left_img = pygame.image.load('graphics/Tile_01.png')
        right_img = pygame.image.load('graphics/Tile_03.png')
        # a number allocated to each tile and that number is put into the 'world_data'
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
                if tile == 2:
                    img = pygame.transform.scale(left_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(right_img, (tile_size, tile_size))
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


# this where the platforms are placed
world_data = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 2, 1, 1, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player = Player(100, screen_height - 190)
world = World(world_data)

run = True
while run:

    clock.tick(fps)

    screen.blit(bg_img, (0, 0))

    world.draw()
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # flipping the display?
    pygame.display.update()

pygame.quit()