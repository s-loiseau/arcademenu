import pygame


class Button:
    def __init__(self, label, x, y, txtcolor, bgcolor, bordercolor, padding, theme, font, menuw, menuh):
        self.w = menuw
        self.h = menuh
        self.label = label
        self.x = x
        self.y = y
        self.font = font
        self.txtcolor = txtcolor
        self.bgcolor = bgcolor
        self.bordercolor = bordercolor
        self.theme = theme
        self.padding = padding
        self.selected = 0


    def debug(self):
        print(self.label, self.x, self.y)


    def drawpoly(self, y, color, width=0):
        surf = pygame.display.get_surface()
        _x = self.x
        _y = y
        _w = self.w - 2 * self.x
        _h = 2 * self.padding + 25
        corner = 15
        self.poly = (
            (_x, _y),
            (_x + _w, _y),
            (_x + _w, _y + _h - corner),
            (_x + _w - corner, _y + _h),
            (_x, _y + _h),
        )
        pygame.draw.polygon(surf, color, self.poly, width)


    def draw2(self):
        surf = pygame.display.get_surface()
        textblock = self.font.render(self.label, True, self.txtcolor)
        self.drawpoly(self.y, self.bgcolor)
        self.drawpoly(self.y, self.bordercolor, 3)
        surf.blit(textblock, (self.x + self.padding, self.y + self.padding))


    def glitch(self):
        surface = pygame.display.get_surface()
        surface.fill((0,233,0))
        rect = pygame.Rect((0,0), (30,220))
        pygame.draw.rect(surface, (22,0,0), rect)
        pygame.display.update()


    def update(self):
        pass
