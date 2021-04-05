#!/usr/bin/env python
import pygame
import os
import sys
from menus import mainmenu


if __name__ == "__main__":
    try:
        pygame.mixer.pre_init(48000, -16, 2, 256)
    except:
        nosound = True
        pass

    pygame.init()

    pygame.key.set_repeat(120,100)
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 10"


    print("MAINMENU main loop")
    mainmenu()

    pygame.quit()
    sys.exit()
