import pygame

pygame.init()

images = dict()
images['TileMap'] = pygame.image.load(
    'Resources/Visual/Textures/Tilemaps/tilemap_export.png'
    )
images['DeadTree'] = pygame.image.load(
    'Resources/Visual/Textures/Sprites/DeadTree.png'
    )
images['Background'] = pygame.image.load(
    'Resources/Visual/Textures/Background/Landscape.jpg'
    )
images['Player'] = pygame.image.load(
    'Resources/Visual/Textures/Sprites/Player.png'
    )
