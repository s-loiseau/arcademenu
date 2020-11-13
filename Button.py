import pygame


class Button:
    def __init__(self, label, x, y, padding, theme, font, menuw, menuh):
        self.selected = 0
        self.w = menuw
        self.h = menuh
        self.label = label
        self.x = x
        self.y = y
        self.font = font
        self.theme = theme
        self.colors = self.theme[self.selected]
        self.txtcolor = self.colors[0]
        self.bgcolor = self.colors[1]
        self.bordercolor = self.colors[2]
        self.padding = padding


    def select(self):
        self.selected = 1
        self.update()

    def unselect(self):
        self.selected = 0
        self.update()


    def drawpoly(self, y, color, width=0):
        surf = pygame.display.get_surface()
        _w = self.w - 2 * self.x
        _h = 2 * self.padding + 30
        corner = 15
        self.poly = (
            (self.x, self.y),
            (self.x + _w, self.y),
            (self.x + _w, self.y + _h - corner),
            (self.x + _w - corner, self.y + _h),
            (self.x, self.y + _h),
        )
        pygame.draw.polygon(surf, color, self.poly, width)
        #pygame.draw.line(surf, color, (0,self.y), (self.w,self.y), 3)
        #pygame.draw.line(surf, color, (0,self.y + _h), (self.w,self.y + _h), 3)


    def draw(self):
        self.update()
        surf = pygame.display.get_surface()
        textblock = self.font.render(self.label, True, self.txtcolor)
        self.drawpoly(self.y, self.bgcolor)
        self.drawpoly(self.y, self.bordercolor, 3)
        surf.blit(textblock, (self.x + self.padding, self.y + self.padding))


    def update(self):
        # change colors
        self.colors = self.theme[self.selected]
        self.txtcolor = self.colors[0]
        self.bgcolor = self.colors[1]
        self.bordercolor = self.colors[2]
