#!/usr/bin/env python
import pygame
import os
import sys
from menus import mainmenu


if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 10"

    mainmenu()

    pygame.quit()
    sys.exit()
