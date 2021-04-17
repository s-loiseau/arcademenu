import pygame
import os

def play(sound):
    sound.stop()
    sound.play()


maindir = os.path.dirname(__file__)
sounddir = os.path.join(maindir, "sounds")

pygame.mixer.pre_init(48000, -16, 2, 256)
pygame.mixer.init()

effect1 = pygame.mixer.Sound(os.path.join(sounddir, "comperror.wav"))
effect1.set_volume(0.1)
effect2 = pygame.mixer.Sound(os.path.join(sounddir, "compstart.wav"))
effect2.set_volume(0.1)
effect3 = pygame.mixer.Sound(os.path.join(sounddir, "robot.wav"))
effect3.set_volume(0.1)
