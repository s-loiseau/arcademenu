import os
import time
import sys
import pygame
from Button import Button
import sounds as s
#from menus import mainmenu


class Menu:
    def __init__(self, menudict, x, y, fontname, theme):
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

        # set color of defaut selection 0
        self.buttons[self.index].select()
        self.draw()


    def fixwindowsize(self):
        # if screen size is not good , set_mode again
        _w, _h = pygame.display.get_window_size()

        if self.w != _h or self.h != _w:
            pygame.display.set_mode((self.w, self.h), vsync=1)



    def draw(self):
        print(self.h, self.w)
        print(pygame.display.get_window_size())
        surf = pygame.display.get_surface()
        surf.fill((0,0,0))
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
        self.draw()

    def enter(self):
        label = self.buttons[self.index].label
        action = self.menudict[label]
        action()
        self.draw()

    def back(self):
        #s.play(s.effect3)
        self.active = False
        #self.update()
        pass


    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    print("QUIT")
                    pygame.quit()
                    sys.exit()
                if e.key == pygame.K_l:
                    self.enter()
                if e.key == pygame.K_h:
                    self.back()
                    self.fixwindowsize()
                if e.key == pygame.K_j:
                    self.next()
                if e.key == pygame.K_k:
                    self.previous()

    def run(self):
        while self.active:
            self.update()
