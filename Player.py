import Entity
import Helper
import pygame
import ImageFiles


class Player(pygame.sprite.Sprite):
    currentLane = 0  # 0: Middle, -1: Left, 1: Right
    displaySurface = Helper.DISPLAY_SURFACE
    playerSurf = ImageFiles.images['Player']
    playerRect = playerSurf.get_rect()
    playerPos = [Helper.RESOLUTION[0] * 0.5 - playerSurf.get_width() * 0.5,
                 Helper.RESOLUTION[1] * 0.2 - playerSurf.get_height() * 0.5
                 + 600
                 ]  # (311.0, 202.8 for 750x1334 resolution)
    moveDistance = Helper.MOVE_DISTANCE

    @staticmethod
    def player_action(action, player, inv_is_open=False):
        if 'move' in action:
            Player.player_move(action, player, inv_is_open)
        elif 'idle' == action:
            pass

    @staticmethod
    def inventory_update(action, is_open=False):
        if 'switch_inv' == action:
            return not is_open
        elif 'open_inv' == action:
            return True
        elif 'close_inv' == action:
            return False
        else:
            return is_open

    @staticmethod
    def player_move(direction, player, inv_is_open=False):  # needs four directions
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
                player.playerPos[0] += Helper.MOVE_SPEED
                Player.displaySurface.blit(ImageFiles.images['Background'], (0, 0))
                Player.displaySurface.blit(player.playerSurf, player.playerPos)
                if inv_is_open:
                    Player.displaySurface.blit(ImageFiles.images['UI']['Inventory_Background'], (0, 0))
                pygame.display.flip()

        elif direction == 'move_left' and player.currentLane > -1:
            player_destination = player.playerPos[0] - player.moveDistance
            player.currentLane -= 1

            while player.playerPos[0] > player_destination:
                player.playerPos[0] -= Helper.MOVE_SPEED  # needs a loop in the "Main" script?
                Player.displaySurface.blit(ImageFiles.images['Background'], (0, 0))
                Player.displaySurface.blit(player.playerSurf, player.playerPos)
                if inv_is_open:
                    Player.displaySurface.blit(ImageFiles.images['UI']['Inventory_Background'], (0, 0))
                pygame.display.flip()
