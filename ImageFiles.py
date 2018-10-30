import pygame

pygame.init()

images = dict()
images['TileMap'] = pygame.image.load(
    'Resources/Visual/Textures/Tilemaps/tilemap_export.png'
    )
images['DeadTree'] = pygame.image.load(
    'Resources/Visual/Textures/Sprites/dead_tree.png'
    )
images['Background'] = pygame.image.load(
    'Resources/Visual/Textures/Background/room0.png'
    )
images['Player'] = pygame.image.load(
    'Resources/Visual/Textures/Sprites/player.png'
    )
