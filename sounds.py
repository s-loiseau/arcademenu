import pygame
from pathlib import Path
import os

maindir = os.path.dirname(__file__)
sounddir= os.path.join(maindir, 'sounds')

pygame.mixer.init()
effect1 = pygame.mixer.Sound(os.path.join(sounddir, "comperror.wav"))
#effect1 = pygame.mixer.Sound(os.path.join(sounddir, "bup.wav"))
effect1.set_volume(0.1)
effect2 = pygame.mixer.Sound(os.path.join(sounddir, "compstart.wav"))
effect2.set_volume(0.1)
effect3 = pygame.mixer.Sound(os.path.join(sounddir, "robot.wav"))
effect3.set_volume(0.1)


def play(sound):
    sound.stop()
    sound.play()

