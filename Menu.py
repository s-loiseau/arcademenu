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

        self.fontsize = 30

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
        for k in self.menudict.keys():
            self.buttons.append(
                Button(k, bx, by, self.padding, self.theme, self.font, self.w, self.h)
            )
            by += self.padding * 2 + self.texth + self.interbutton

        pygame.display.set_mode((self.w, self.h), vsync=1)

        self.surf = pygame.display.get_surface()

        # set color of defaut selection 0
        self.buttons[self.index].select()
        self.draw()


    def fixwindowsize(self):
        # if screen size is not good , set_mode again
        _w, _h = pygame.display.get_window_size()

        if self.w != _w or self.h != _h:
            print("FIX RESIZE", self.w, self.h, _w, _h)
            pygame.display.set_mode((self.w, self.h), vsync=1)



    def draw(self):
        self.surf = pygame.display.get_surface()
        self.fixwindowsize()

        self.surf.fill((0,0,0))
        for b in self.buttons:
            b.draw()
        pygame.display.flip()


    def next(self):
        if self.index < len(self.buttons) - 1:
            self.move(1)

    def previous(self):
        if self.index > 0:
            self.move(-1)

    def move(self,direction):
        s.play(s.effect1)
        self.buttons[self.index].unselect()
        self.index = self.index + direction
        self.buttons[self.index].select()



    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    print("QUIT")
                    time.sleep(0.2)
                    pygame.quit()
                    sys.exit()

                elif pygame.key.get_pressed()[pygame.K_l]:
                    s.play(s.effect3)
                    label = self.buttons[self.index].label
                    time.sleep(0.05)

                    print(type(self.menudict[label]))
                    print(self.menudict[label])

                    if type(self.menudict[label]) == tuple:
                        self.menudict[label][0](self.menudict[label][1])
                    else:
                        self.menudict[label]()

                elif e.key == pygame.K_h:
                    s.play(s.effect3)
                    time.sleep(0.05)
                    self.active = False

                elif e.key == pygame.K_j:
                    self.buttons[self.index].blink(3)
                    self.next()

                elif e.key == pygame.K_k:
                    self.buttons[self.index].blink(2)
                    self.previous()



    def run(self):
        while self.active:
            self.clock.tick(30)
            self.update()
            self.draw()
