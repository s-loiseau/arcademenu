import os
import sys
import pygame
from button import button
import menus as m
from themes import theme1
import sounds as s


def back():
    s.play(s.effect3)
    print("BACK MAIN MENU")
    menu(m.mainmenudict, 0, 0, "VCR.ttf", theme1).run()


def pinpon():
    print("PINPONPINPON")
    #os.system("urxvt")


def submenu():
    print("SUB MENU")
    menu(m.submenudict, 0, 0, "hiragana tfb.ttf", theme1).run()


actions = {"POLICE": pinpon, "SUBMENU": submenu}


class menu:
    def __init__(self, menudict, x, y, fontname, theme):
        maindir = os.path.dirname(__file__)
        fontdir = os.path.join(maindir, "fonts")
        self.fontname = fontname
        self.theme = theme

        self.fontsize = 30

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.index = 0
        self.menudict = menudict
        self.x = x
        self.y = y

        self.padding = 10
        self.border = 10
        self.interbutton = 10

        # BASIC COLORS
        self.txt = self.theme["txt"]
        self.bg = self.theme["bg"]
        self.brdr = self.theme["border"]
        # SELECT COLORS
        self.selecttxt = self.theme["stxt"]
        self.selectbg = self.theme["sbg"]
        self.selectborder = self.theme["sborder"]

        self.larger_label = max([len(x) for x in self.menudict.keys()])
        # GUESS DIMENSIONS FONT :
        self.font = pygame.font.Font(
            os.path.join(fontdir, self.fontname), self.fontsize
        )
        _, _, self.textw, self.texth = self.font.render(
            self.larger_label * "X", True, (0, 0, 0)
        ).get_rect()
        print("sizeblock", self.textw, self.texth)

        self.buttons = []
        bx, by = self.border, self.border
        for k in self.menudict.keys():
            self.buttons.append(button(k, bx, by, self.txt, self.bg, self.brdr))
            by += self.padding * 2 + self.texth + self.interbutton

        self.w = self.textw + 2 * self.border + 2 * self.padding
        self.h = (
            (2 * self.border)
            + (len(self.buttons) * (self.texth + 2 * self.padding))
            + ((len(self.buttons) - 1) * self.interbutton)
        )

        pygame.display.set_mode((self.w, self.h))
        # set color of defaut selection 0
        self.select()
        self.draw()


    def drawpoly(self, y, color, width=0):
        surf = pygame.display.get_surface()
        _x = self.border
        _y = y
        _w = self.w - 2 * self.border
        _h = 2 * self.padding + self.texth
        corner = 15
        self.poly = (
            (_x, _y),
            (_x + _w, _y),
            (_x + _w, _y + _h - corner),
            (_x + _w - corner, _y + _h),
            (_x, _y + _h),
        )
        pygame.draw.polygon(surf, color, self.poly, width)


    def draw(self):
        # pygame.display.set_mode((self.w, self.h))
        surf = pygame.display.get_surface()
        surf.fill((0, 0, 0))
        for b in self.buttons:
            textblock = self.font.render(b.label, True, b.txtcolor)
            self.drawpoly(b.y, b.bgcolor)
            self.drawpoly(b.y, b.bordercolor, 3)
            surf.blit(textblock, (self.border + self.padding, b.y + self.padding))


    def select(self):
        self.buttons[self.index].txtcolor = self.selecttxt
        self.buttons[self.index].bgcolor = self.selectbg
        self.buttons[self.index].bordercolor = self.selectborder


    def unselect(self):
        self.buttons[self.index].txtcolor = self.txt
        self.buttons[self.index].bgcolor = self.bg
        self.buttons[self.index].bordercolor = self.brdr


    def next(self):
        s.play(s.effect3)
        if self.index < len(self.buttons) - 1:
            self.unselect()
            self.index += 1
            self.select()
        self.draw()


    def previous(self):
        s.play(s.effect3)
        if self.index > 0:
            self.unselect()
            self.index -= 1
            self.select()
        self.draw()


    def enter(self):
        print("ENTER", self.index)
        label = self.buttons[self.index].label
        # exec
        self.blink(4)
        action = self.menudict[label]
        actions[action]()


    def back(self):
        print("BACK", self.index)
        back()


    def blink(self, blinks):
        s.play(s.effect1)
        for x in range(blinks):
            self.clock.tick(self.FPS)
            print("BLINK")
            self.unselect()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.FPS)
            print("BLINK2")
            self.select()
            self.draw()
            pygame.display.update()


    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    print("QUIT")
                    pygame.quit()
                    sys.exit()
                elif e.key == pygame.K_j:
                    self.next()
                elif e.key == pygame.K_k:
                    self.previous()
                elif e.key == pygame.K_l:
                    self.enter()
                elif e.key == pygame.K_h:
                    self.back()


    def run(self):
        while True:
            pygame.display.update()
            self.clock.tick(self.FPS)
            self.update()
