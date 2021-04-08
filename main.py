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

    surf = pygame.display.get_surface()

    done = False
    while not done:
        clock.tick(60)
        ecran = gamedict[activescreen]

        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            ecran.update(event)


        #DRAW
        surf.fill((0,0,0))
        ecran.draw()

    pygame.quit()
    sys.exit()
