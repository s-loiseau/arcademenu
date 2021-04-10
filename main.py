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


    clock = pygame.time.Clock()
    
    activescreen = 'mainmenu'

    gamedict = {'mainmenu':mainmenu(),
                'powermenu':powermenu()}

    surf = pygame.display.get_surface()

    done = False
    ecran = gamedict[activescreen]
    while not done:
        clock.tick(20)

        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            activescreen = ecran.update(event)
            if activescreen:
                print(activescreen, "receive, should load it")
                ecran = gamedict[activescreen]


        #DRAW
        surf.fill((0,0,0))
        ecran.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()
