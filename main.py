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

    os.environ["SDL_VIDEO_WINDOW_POS"] = "1, 1"

    pygame.key.set_repeat(120,60)

    clock = pygame.time.Clock()

    activescreen = 'mainmenu'

    gamedict = {'mainmenu':mainmenu(),
                'powermenu':powermenu(), 
                'interactivemenu':interactivemenu(),
                'audiomenu':audiomenu(),
                'hdmimenu':hdmimenu(),
                'ivideo':ivideo()
               }

    surf = pygame.display.get_surface()

    done = False
    ecran = gamedict[activescreen]
    while not done:
        clock.tick(60)

        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            activescreen = ecran.update(event)
            if activescreen:
                # slow down to avoid multiple actions too quickly.
                pygame.time.wait(100)
                print(activescreen, "receive, should load it")
                ecran = gamedict[activescreen]


        #DRAW
        surf.fill((0,0,0))
        ecran.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()
