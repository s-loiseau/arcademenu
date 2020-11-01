#!/usr/bin/env python
import pygame
import os
import sys
import time
from menu import menu
from menus import mainmenudict
from themes import theme1


if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    # window = pygame.display.set_mode((50, 50))
    # os.environ["SDL_VIDEO_WINDOW_POS"] = "410, 10"
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 10"
    #os.environ["SDL_VIDEO_CENTERED"] = "1"

    menu(mainmenudict, 0, 0, "VCR.ttf", theme1).run()

    pygame.quit()
    sys.exit()
