import os
import time
import sys
import pygame

import sounds as s
from Button import Button


class Menu:
    def __init__(self, menudict, x, y, fontname, theme):
        self.clock = pygame.time.Clock()
        maindir = os.path.dirname(__file__)
        fontdir = os.path.join(maindir, "fonts")
        self.fontname = fontname
        self.theme = theme

        self.fontsize = 20

        self.active = True

        self.index = 0

        self.menudict = menudict
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

        #print("sizeblock", self.textw, self.texth)

        self.w = self.textw + 2 * self.border + 2 * self.padding
        self.h = (
            (2 * self.border)
            + (len(self.menudict.keys()) * (self.texth + 2 * self.padding))
            + ((len(self.menudict.keys()) - 1) * self.interbutton)
            + self.border
        )

        self.buttons = []
        bx, by = self.border, self.border
        self.intervalbutton = self.padding * 2 + self.texth + self.interbutton
        for k in self.menudict.keys():
            self.buttons.append(
                Button(k, bx, by, self.padding, self.theme, self.font, self.w, self.h)
            )
            #by += self.padding * 2 + self.texth + self.interbutton
            by += self.intervalbutton

        pygame.display.set_mode((self.w, self.h), vsync=1)

        self.buttons[self.index].select()
        self.draw()

    def fixwindowsize(self):
        # if screen size is not good , set_mode again
        _w, _h = pygame.display.get_window_size()

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
            if checky >= screenh - self.intervalbutton:
                print(checky, self.index)
                for b in self.buttons:
                    b.y -= self.intervalbutton

    def previous(self):
        if self.index > 0:
            self.move(-1)
            checky = self.buttons[self.index].y
            #increment = 58
            increment = self.intervalbutton
            if checky < 0:
                print(checky, self.index)
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

                print(type(action), label)

                if isinstance(action,tuple):
                    print("ACTION", action)
                    action[0](action[1])
                    return None
                elif callable(action):
                    action()
                else:
                    return action

            elif e.key == pygame.K_h:
                s.play(s.effect3)
                self.active = False
                return 'mainmenu'

            elif e.key == pygame.K_j:
                self.next()

            elif e.key == pygame.K_k:
                self.previous()
