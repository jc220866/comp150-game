import pygame
import random
import sys
import wave
import math
import struct
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 1, 4096)  # frequency, size, channels, buffersize
pygame.init()

AudioDict = dict()
AudioDict['UI_click_settings'] = pygame.mixer.Sound('./Resources/Audio/User_Interface/menu_click_settings.wav')
AudioDict['UI_click_grayedout'] = pygame.mixer.Sound('./Resources/Audio/User_Interface/menu_click_grayedout.wav')

COMP_TYPE = "NONE"
COMP_NAME = "not compressed"
PI = math.pi
VOLUME = 1
N_CHANNELS = 1
SAMPLE_WIDTH = 2
FRAMERATE = 44100  # SAMPLE_RATE
N_FRAMES = 5000  # SAMPLE_LENGTH
AMPLITUDE = 4096  # BIT_DEPTH


def set_wave_parameters(sound):
    sound.setparams((
        N_CHANNELS,
        SAMPLE_WIDTH,
        FRAMERATE,
        N_FRAMES,
        COMP_TYPE,
        COMP_NAME
        ))


def generate_audio_contents(sound, frequency):
    values = []

    for i in range(0, N_FRAMES):
        value = math.sin(2.0 * PI * frequency *
                         (i / float(FRAMERATE))) * \
                         (VOLUME * AMPLITUDE)
        packaged_value = struct.pack("i", int(value))

        for j in range(0, N_CHANNELS):
            values.append(packaged_value)

    value_str = b''.join(values)
    sound.writeframes(value_str)
    sound.close()


def generate_userinterface_sounds():
    menu_click_settings_frequency = 1000
    menu_click_grayedout_frequency = 200

    menu_click_settings_output = wave.open('./Resources/Audio/User_Interface/menu_click_settings.wav', 'wb')
    menu_click_grayedout_output = wave.open('./Resources/Audio/User_Interface/menu_click_grayedout.wav', 'wb')

    set_wave_parameters(menu_click_settings_output)
    set_wave_parameters(menu_click_grayedout_output)

    generate_audio_contents(menu_click_settings_output,
                            menu_click_settings_frequency)
    generate_audio_contents(menu_click_grayedout_output,
                            menu_click_grayedout_frequency)

    print('UI sounds generated successfully')
