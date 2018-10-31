import Entity
import Helper
import pygame
import ImageFiles


class Player(pygame.sprite.Sprite):
    currentLane = 0  # 0: Middle, -1: Left, 1: Right
    displaySurface = Helper.displaySurface
    playerSurf = ImageFiles.images['Player']
    playerRect = playerSurf.get_rect()
    playerPos = [Helper.RESOLUTION[0] * 0.5 - playerSurf.get_width() * 0.5,
                 Helper.RESOLUTION[1] * 0.2 - playerSurf.get_height() * 0.5
                 + 250
                 ]  # (311.0, 202.8 for 750x1334 resolution)
    moveDistance = Helper.MOVE_DISTANCE

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = 'player'
        self.images = []
        self.image = ImageFiles.images['Player']

        self.rect = self.image.get_rect()

        self.movex = 0  # x axis movement
        self.movey = 0  # y axis movement
        self.frame = 0  # count frames

    def move(self, x, y):
        # Movement control
        self.movex += x
        self.movey += y

    def update(self):
        # sprite position update
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

    @staticmethod
    def player_action(action, player):
        if 'move' in action:
            Player.player_move(action, player)
        elif 'idle' == action:
            pass

    @staticmethod
    def player_move(direction, player):  # needs four directions
        """
        Used for moving player upon swipe input, in future
        will be used for moving from room to room also.

        Args:
            direction -- string of the direction to move
            player -- this player class
        """
        if direction == 'move_right' and player.currentLane < 1:
            player_destination = player.playerPos[0] + player.moveDistance
            player.currentLane += 1

            while player.playerPos[0] < player_destination:
                player.playerPos[0] += Helper.MOVE_SPEED  # needs a loop in the "Main" script?
                Player.displaySurface.blit(ImageFiles.images['Background'], (0, 0))
                Player.displaySurface.blit(player.image, (player.playerPos[0], player.playerPos[1]))
                pygame.display.flip()

        elif direction == 'move_left' and player.currentLane > -1:
            player_destination = player.playerPos[0] - player.moveDistance
            player.currentLane -= 1

            while player.playerPos[0] > player_destination:
                player.playerPos[0] -= Helper.MOVE_SPEED  # needs a loop in the "Main" script?
                Player.displaySurface.blit(ImageFiles.images['Background'], (0, 0))
                Player.displaySurface.blit(player.image, (player.playerPos[0], player.playerPos[1]))

                pygame.display.flip()

