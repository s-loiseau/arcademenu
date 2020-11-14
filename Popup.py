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
        self.w = 200
        self.h = 140
        self.label = "POPUP"
        self.txtcolor = (154,255,123)
        self.active = True
        self.x = 10
        self.y = 20


    def update(self):
        for e in pygame.event.get():

            # key that can be held.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q] or keys[pygame.K_h]:
                self.active = False


    def draw(self):
        print("DRAW POPUP")
        pygame.display.set_mode((self.w + 50,self.h + 50))
        self.update()
        surf = pygame.display.get_surface()
        pygame.draw.rect(surf, self.txtcolor, pygame.Rect(self.x,self.y,self.w,self.h))
        pygame.draw.rect(surf, (100,22,255), pygame.Rect(self.x,self.y,self.w,self.h),10)

        textobj = self.font.render( self.data, True, (255, 0, 0))
        surf.blit(textobj, (self.x + 5,self.y + 5))

        pygame.display.update()


    def run(self):
        self.draw()
        while self.active:
            self.update()

