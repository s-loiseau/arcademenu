#!/usr/bin/env python
import pygame
import os
import sys
from menus import *


if __name__ == "__main__":
    try:
        pygame.mixer.pre_init(48000, -16, 2, 256)
    except:
        nosound = True
        pass

    pygame.init()

    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 10"

    pygame.key.set_repeat(120,100)

    gamedict = {'mainmenu':mainmenu(),
                'powermenu':powermenu()}

    clock = pygame.time.Clock()
    
    activescreen = 'mainmenu'

    while True:
        clock.tick(60)
        ecran = gamedict[activescreen]
        for e in pygame.event.get():
            ecran.update(e)
        ecran.draw()

    pygame.quit()
    sys.exit()
