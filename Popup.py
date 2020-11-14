import pygame


class Popup():
    def __init__(self, w, h, data):
        self.data = data
        self.w = w
        self.h = h
        self.label = "POPUP"
        self.txtcolor = (154,255,123)

    def update(self):
        pass


    def draw(self):
        self.update()
        surf = pygame.display.get_surface()
        pygame.draw.rect(surf, self.txtcolor, pygame.Rect(10,20,200,140))
        pygame.display.update()

