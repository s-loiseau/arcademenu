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


    def debug(self):
        print(self.label, self.x, self.y)
        print(self.colors)


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
        self.debug()
        surf = pygame.display.get_surface()
        textblock = self.font.render(self.label, True, self.txtcolor)
        self.drawpoly(self.y, self.bgcolor)
        self.drawpoly(self.y, self.bordercolor, 3)
        surf.blit(textblock, (self.x + self.padding, self.y + self.padding))


    def glitch(self):
        surf = pygame.display.get_surface()
        surf.fill((0,233,0))
        rect = pygame.Rect((0,0), (30,220))
        pygame.draw.rect(surf, (22,0,0), rect)
        #pygame.display.update()


    def update(self):
        # change colors
        self.colors = self.theme[self.selected]
        self.txtcolor = self.colors[0]
        self.bgcolor = self.colors[1]
        self.bordercolor = self.colors[2]
