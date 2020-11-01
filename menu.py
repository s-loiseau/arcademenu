import os
import sys
import pygame
from button import button
import menus as m
from themes import theme1, theme2
import sounds as s


def video():
    os.system("mpv --really-quiet /home/krao/Videos/joueurdugrenierrage.mp4")


def ok():
    True


def terminal():
    os.system("urxvt")


def hdmionly():
    os.system("~/.screenlayout/onlyhdmi19.sh")


def hdmi():
    os.system("~/.screenlayout/1920hdmi2.sh")


def transmission():
    popup("git status", button.width, button.mheight)


def ls():
    popup("ls -Ggh", button.width, button.mheight)


def netstat():
    popup('netstat -ant', button.width, button.mheight)


def mail():
    os.system("urxvt -e bash -c 'mutt'")


def popup(command, pw, ph):
    # Render cmd result, with multilines
    font = pygame.font.Font(os.path.join(fontdir,"3270-Regular.ttf"), 20)
    txtcolor = (0, 0, 0)
    fillcolor = (205, 205, 0)

    data = subprocess.check_output(command, shell=True)
    data = data.splitlines()

    textblocks = []
    maxlen = 0

    # Generate textblock and evaluate width.
    for l in data:
        textblock = font.render(l, True, txtcolor)
        lab_len = textblock.get_width()
        if lab_len > maxlen:
            maxlen = lab_len
        textblocks.append(textblock)

    # evaluate height.
    linevert = textblocks[0].get_height()
    lines = len(data)
    textvert = linevert * lines + 40


    # Should get width of Calliing button to determine left.
    left = pw + 10
    top = 0
    right = left + maxlen + 10
    bot = top + textvert
    corner = 15
    # Could be nice to create shapes.py.
    poly = (
        (left, bot),
        (left, top),
        (right, top),
        (right, bot - corner),
        (right - corner, bot),
    )

    if textvert  + corner < ph:
        textvert = ph
    else:
        textvert = textvert + corner

    surf = pygame.display.get_surface()
    pygame.display.set_mode((right, textvert))
    surf.fill((10, 10, 10))
    shape = pygame.draw.polygon(surf, fillcolor, poly)
    cursor = [left + 5, top + 5]
    # Draw text
    for t in textblocks:
        # increase y
        cursor[1] += linevert
        surf.blit(t, (cursor))


def pavucontrol():
    os.system("pavucontrol")


def web(button):
    os.system("qutebrowser www.reddit.com/r/france/new")


def back():
    s.play(s.effect3)
    menu(m.mainmenudict, 0, 0, "VCR.ttf", theme1).run()


def poweroff():
    os.system("poweroff")


def hdmimenu():
    # HDMI_ONLY
    # HDMI_ON
    # HDMI_OFF
    menu(m.hdmimenudict, 0, 0, "VCR.ttf", theme1).run()


def powermenu():
    # POWEROFF
    menu(m.powermenudict, 0, 0, "VCR.ttf", theme2).run()


actions = {
           "HDMIMENU": hdmimenu,
           "POWERMENU": powermenu,
           "AUDIO": pavucontrol,
           "POWEROFF": powermenu,
           }


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
        self.border = 5
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
        print("ENTER", self.index)
        s.play(s.effect3)
        # use directly index to find action.
        label = self.buttons[self.index].label
        # exec
        self.blink(4)
        action = self.menudict[label]
        actions[action]()


    def back(self):
        print("BACK", self.index)
        back()


    def blink(self, blinks):
        #s.play(s.effect1)
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
                if e.key == pygame.K_j:
                    self.next()
                if e.key == pygame.K_k:
                    self.previous()
                if e.key == pygame.K_l:
                    self.enter()
                if e.key == pygame.K_h:
                    self.back()


    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.update()
            pygame.display.flip()
