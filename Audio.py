import pygame

def music_loop():
    pygame.mixer_music.load()
    pygame.mixer_music.play(-1)

def pause():
    pygame.mixer_music.pause()
    pause_text = pygame.font.SysFont(Helvetica, 24)
    TextSurf, TextRect =

def unpause():
    global pause()
    pygame.mixer_music.unpause()
    pause = false

def sword_sound():
    pygame.mixer_music.stop()
    sword_swing = pygame.mixer.Sound()
    pygame.mixer_music.play(sword_swing)
