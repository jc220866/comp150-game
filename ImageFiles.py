import pygame

pygame.init()

images = dict()
images['Tilemap'] = pygame.image.load(
    'Resources/Visual/Textures/Tilemaps/tilemap_export.png'
    )

images['DeadTree'] = pygame.image.load(
    'Resources/Visual/Textures/Sprites/dead_tree.png'
    )

images['Background'] = pygame.image.load(
    'Resources/Visual/Textures/Rooms/room.png'
    )

images['Player'] = pygame.image.load(
    'Resources/Visual/Textures/Sprites/player.png'
    )
