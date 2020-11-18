import pygame
import os
import textwrap


class Popup():
    def __init__(self, data, font):
        maindir = os.path.dirname(__file__)
        fontdir = os.path.join(maindir, "fonts")
        self.fontsize = 30
        self.fontname = font
        self.font = pygame.font.Font( os.path.join(fontdir, self.fontname), self.fontsize)
        self.data = data.splitlines()

        self.wrap = []
        for line in self.data:
            self.wrap.append(textwrap.wrap(line, width=80))


        self.w = 0
        self.h = self.font.render("X", True, (255, 255, 0)).get_rect()[-1]
        self.label = "POPUP"
        self.txtcolor = (154,255,123)
        self.active = True
        self.padding = 0
        self.x = self.padding
        self.y = self.padding
        self.cursor = 0
        self.scroll = 0
        self.scroll += self.h
        self.clock = pygame.time.Clock()
        self.FPS = 10


    def update(self):
        for e in pygame.event.get():

            # key that can be held.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] or keys[pygame.K_h]:
                self.active = False
                self.draw()
            if keys[pygame.K_j]:
                self.scroll -= self.h
                self.draw()
                continue
            elif keys[pygame.K_k]:
                self.scroll += self.h
                self.draw()
                continue
            if keys[pygame.K_l]:
                self.scroll = 0
                self.draw()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_j:
                    self.scroll -= self.h
                if e.key == pygame.K_k:
                    self.scroll += self.h
                if e.key == pygame.K_SPACE:
                    self.scroll -=  5 * self.h
                self.draw()


    def draw(self):
        print("DRAW POPUP")

        maxlen = 0
        textobjs = []
        for l in self.wrap:
            for line in l:
                print(line, type(line))
                textobj = self.font.render( line, True, (255, 255, 0))
                textobjs.append(textobj)
                w = textobj.get_rect()[2]
                if w > maxlen:
                    maxlen = w

        #self.padding = self.h
        # Limit maxw and maxh.
        nblines = len(textobjs)
        winh = nblines * self.h + self.h + self.padding
        if winh > 1000:
            winh = 1000

        if maxlen > 1900:
            maxlen = 1900

        pygame.display.set_mode((maxlen + 2 * self.h, winh))

        y = self.scroll
        surf = pygame.display.get_surface()
        textobj = textobjs[0]
        pygame.draw.rect(surf, (244,34,244), pygame.Rect(self.x, self.h, maxlen, self.h ))
        surf.blit(textobj, (self.x ,y))
        y += self.h

        for textobj in textobjs[1:]:
            w, h = textobj.get_rect()[2:]
            surf.blit(textobj, (self.x + 5,y))
            y += h

        pygame.display.update()


    def run(self):
        self.draw()
        while self.active:
            self.clock.tick(self.FPS)
            self.update()

