import os
import sys
import pygame
from Button import Button
import sounds as s



class Menu:
    def __init__(self, menudict, x, y, fontname, theme):
        maindir = os.path.dirname(__file__)
        self.active = True
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
        self.border = 5
        self.interbutton = 10

        # TODO: Should call theme items directly, and litteraly be managed in Button class.
        # SELECT COLORS

        self.larger_label = max([len(x) for x in self.menudict.keys()])
        # GUESS DIMENSIONS FONT :
        self.font = pygame.font.Font(
            os.path.join(fontdir, self.fontname), self.fontsize
        )
        _, _, self.textw, self.texth = self.font.render(
            self.larger_label * "X", True, (0, 0, 0)
        ).get_rect()
        print("sizeblock", self.textw, self.texth)

        self.w = self.textw + 2 * self.border + 2 * self.padding
        self.h = (
            (2 * self.border)
            + (len(self.menudict.keys()) * (self.texth + 2 * self.padding))
            + ((len(self.menudict.keys()) - 1) * self.interbutton)
        )
        print("sizeblock", self.w, self.h)

        self.buttons = []
        bx, by = self.border, self.border
        for k in self.menudict.keys():
            self.buttons.append(Button(k, bx, by, self.padding, self.theme, self.font, self.w, self.h))
            by += self.padding * 2 + self.texth + self.interbutton


        pygame.display.set_mode((self.w, self.h))
        # set color of defaut selection 0
        self.select()
        self.draw()



    def draw(self):
        surf = pygame.display.get_surface()
        surf.fill((0, 0, 0))
        for b in self.buttons:
            b.draw()

    def select(self):
        self.buttons[self.index].selected = 1


    def next(self):
        s.play(s.effect1)


    def unselect(self):
        self.buttons[self.index].selected = 0



    def next(self):
        s.play(s.effect1)
        self.blink(2)
        if self.index < len(self.buttons) - 1:
            self.unselect()
            self.index += 1
            self.select()
        self.draw()


    def previous(self):
        s.play(s.effect1)
        self.blink(2)
        if self.index > 0:
            self.unselect()
            self.index -= 1
            self.select()
        self.draw()


    def enter(self):
        s.play(s.effect3)
        label = self.buttons[self.index].label
        self.blink(4)
        action = self.menudict[label]
        action()


    def back(self):
        self.active = False


    def blink(self, blinks):
        for x in range(blinks):
            self.clock.tick(self.FPS)
            self.unselect()
            self.draw()
            pygame.display.update()

            self.clock.tick(self.FPS)
            self.select()
            self.draw()
            pygame.display.update()
        self.buttons[0].draw()


    def update(self):
        for e in pygame.event.get():
            print("DRAW")
            pygame.display.set_mode((self.w, self.h))
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    print("QUIT")
                    pygame.quit()
                    sys.exit()
                if e.key == pygame.K_j:
                    self.next()
                if e.key == pygame.K_k:
                    self.previous()
                if e.key == pygame.K_l:
                    self.enter()
                if e.key == pygame.K_h:
                    self.back()


    def run(self):
        while self.active:
            self.clock.tick(self.FPS)
            self.update()
            self.draw()
            pygame.display.flip()
