import os
import time
import sys
import pygame

import sounds as s
from Button import Button


class Menu:
    def __init__(self, menudict, x, y, fontname, theme, back='mainmenu'):
        self.clock = pygame.time.Clock()
        maindir = os.path.dirname(__file__)
        fontdir = os.path.join(maindir, "fonts")
        self.back = back
        self.fontname = fontname
        self.theme = theme

        self.fontsize = 30

        self.active = True

        self.index = 0

        self.menudict = menudict
        self.nbbuttons = len(self.menudict.keys())
        self.x = x
        self.y = y

        self.padding = 10
        self.border = 5
        self.interbutton = 10

        self.larger_label = max([len(x) for x in self.menudict.keys()])

        # GUESS DIMENSIONS FONT :
        self.font = pygame.font.Font(
            os.path.join(fontdir, self.fontname), self.fontsize
        )

        _, _, self.textw, self.texth = self.font.render(
            self.larger_label * "X", True, (0, 0, 0)
        ).get_rect()

        self.w = self.textw + 2 * self.border + 2 * self.padding
        self.h = (
            (2 * self.border)
            + (self.nbbuttons * (self.texth + 2 * self.padding))
            + ((self.nbbuttons - 1) * self.interbutton)
            + self.border
        )

        self.buttons = []
        bx, by = self.border, self.border
        self.intervalbutton = self.padding * 2 + self.texth + self.interbutton
        for k in self.menudict.keys():
            self.buttons.append(
                Button(k, bx, by, self.padding, self.theme, self.font, self.w, self.h)
            )
            by += self.intervalbutton

        self.maxh = 1026
        if self.h > self.maxh:
            self.h = self.maxh

        self.buttons[self.index].select()

    def fixwindowsize(self):
        # if screen size is not good , set_mode again
        _w, _h = pygame.display.get_window_size()
        if self.h > self.maxh:
            self.h = self.maxh

        if self.w != _w or self.h != _h:
            print("FIX RESIZE", self.w, self.h, _w, _h)
            pygame.display.set_mode((self.w, self.h), vsync=1)

    def draw(self):
        self.fixwindowsize()

        for b in self.buttons:
            b.draw()

    def next(self):
        if self.index < len(self.buttons) - 1:
            self.move(1)
            checky = self.buttons[self.index].y
            increment = self.intervalbutton
            _w, _h = pygame.display.get_window_size()
            screenh = pygame.display.get_desktop_sizes()[0][1]

            if self.index < len(self.buttons) - 1:
                if checky >= screenh - 2 * self.intervalbutton:
                    for b in self.buttons:
                        b.y -= self.intervalbutton

    def previous(self):
        if self.index > 0:
            self.move(-1)
            checky = self.buttons[self.index].y
            #increment = 58
            increment = self.intervalbutton
            if checky < 0:
                for b in self.buttons:
                    b.y += self.intervalbutton

    def move(self,direction):
        s.play(s.effect1)
        self.buttons[self.index].unselect()
        self.index = self.index + direction
        self.buttons[self.index].select()

    def update(self,event):
        e = event
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                print("QUIT")
                pygame.quit()
                sys.exit()

            elif pygame.key.get_pressed()[pygame.K_l]:
                s.play(s.effect3)


                label = self.buttons[self.index].label
                action = self.menudict[label]

                if isinstance(action,tuple):
                    action[0](action[1])
                    return None
                elif callable(action):
                    action()
                else:
                    return action

            elif e.key == pygame.K_h:
                s.play(s.effect3)
                self.active = False
                return self.back 

            elif e.key == pygame.K_j:
                self.next()

            elif e.key == pygame.K_k:
                self.previous()

            elif e.key == pygame.K_SPACE:
                self.next()
                self.next()
                self.next()
                self.next()
