import pygame
import os


class Popup():
    def __init__(self, data, font):
        maindir = os.path.dirname(__file__)
        fontdir = os.path.join(maindir, "fonts")
        self.fontsize = 30
        self.fontname = font
        self.font = pygame.font.Font( os.path.join(fontdir, self.fontname), self.fontsize)
        self.data = data
        self.w = 0
        self.h = 0
        self.label = "POPUP"
        self.txtcolor = (154,255,123)
        self.active = True
        self.x = 10
        self.y = 20
        self.scroll = 0
        self.clock = pygame.time.Clock()
        self.FPS = 10


    def update(self):
        for e in pygame.event.get():

            # key that can be held.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] or keys[pygame.K_h]:
                self.active = False
            if keys[pygame.K_j]:
                self.scroll -= 0
                self.draw()
            elif keys[pygame.K_k]:
                self.scroll += 0
                self.draw()
            if keys[pygame.K_l]:
                self.scroll = 0
                self.draw()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_j:
                    self.scroll -= 28
                if e.key == pygame.K_k:
                    self.scroll += 28
                if e.key == pygame.K_SPACE:
                    self.scroll -=  5 * 28
                self.draw()


    def draw(self):
        print("DRAW POPUP")

        maxlen = 0
        textobjs = []
        for l in self.data:
            textobj = self.font.render( l.decode(), True, (255, 255, 0))
            textobjs.append(textobj)
            w, h = textobj.get_rect()[2:]
            if w > maxlen:
                maxlen = w

        pygame.display.set_mode((maxlen + h, len(self.data) * h + h))

        y = self.y + 5 + self.scroll
        surf = pygame.display.get_surface()
        textobj = textobjs[0]
        pygame.draw.rect(surf, (244,34,244), pygame.Rect(self.x,self.y, maxlen, h + 10))
        surf.blit(textobj, (self.x + 5,y))
        y += h

        for textobj in textobjs[1:]:
            w, h = textobj.get_rect()[2:]
            #pygame.draw.rect(surf, (244,34,244), pygame.Rect(self.x,self.y,w,h + 10))
            surf.blit(textobj, (self.x + 5,y))
            y += h

        pygame.display.update()


    def run(self):
        self.draw()
        while self.active:
            self.clock.tick(self.FPS)
            self.update()

