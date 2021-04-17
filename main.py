#!/usr/bin/env python
import pygame
import os
import sys
import menus as m


if __name__ == "__main__":
    try:
        pygame.mixer.pre_init(48000, -16, 2, 256)
    except:
        nosound = True
        pass

    pygame.init()

    os.environ["SDL_VIDEO_WINDOW_POS"] = "1, 1"

    pygame.key.set_repeat(120,80)

    clock = pygame.time.Clock()

    activescreen = 'mainmenu'

    gamedict = {'mainmenu':m.mainmenu,
                'powermenu':m.powermenu, 
                'interactivemenu':m.interactivemenu,
                'audiomenu':m.audiomenu,
                'hdmimenu':m.hdmimenu,
                'ivideo':m.ivideo
               }


    done = False

    ecran = gamedict[activescreen]()

    print("START",ecran.h, ecran.w)

    surf = pygame.display.set_mode((ecran.w, ecran.h), vsync=1)

    #surf = pygame.display.get_surface()

    # LOOP
    while not done:
        clock.tick(30)

        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                activescreen = ecran.update(event)
                if activescreen:
                    # slow down to avoid multiple actions too quickly.
                    pygame.time.wait(100)
                    print(activescreen, "CHANGE MENU")
                    ecran = gamedict[activescreen]()

            #DRAW
            surf.fill((0,0,0))
            ecran.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()
