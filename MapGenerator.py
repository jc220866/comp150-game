import pygame
import os

"""Map Generation, including tile separation"""

pygame.init()

windowHeight = 150
windowWidth = 450

screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('Map Generation')

tilemap = pygame.image.load(
    './Resources/Visual/Textures/Tilemaps/Tilemap_export.png').convert_alpha()
tile_path = './Resources/Visual/Textures/Tiles/'

# Number of tiles on the x and y axis
tilemap_size_x = 9
tilemap_size_y = 9

# Index keeps track of each tile
tile_index = 0


# Function for removing empty tiles from directory
def empty_tile_removal(path):

    for filename in os.listdir(path):
        if filename.endswith('.png'):
            image = pygame.image.load(path + filename)
            is_empty = True
            for x in range(0, image.get_width()):
                for y in range(0, image.get_height()):
                    if image.get_at((x, y)).a != 0:
                        is_empty = False
                        break
            if is_empty:
                os.remove(path + filename)


# Separator for tiles
def separate_tiles(size_x, size_y, tilemap, path, index):
    for x in range(0, size_x):
        for y in range(0, size_y):

            tile_area = pygame.Rect(y * 25, x * 25, 24, 24)
            tile = tilemap.subsurface(tile_area)
            pygame.image.save(tile, path + 'Tile' + str(index) + '.png')
            index += 1

    print('Finished splitting')

    empty_tile_removal(path)

    print('Finished removing empty tiles')


finished = False

while finished is False:    # Basic game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        # when 'g' is pressed a random item is generated
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            separate_tiles(tilemap_size_x, tilemap_size_y, tilemap, tile_path, tile_index)
        pygame.display.update()
