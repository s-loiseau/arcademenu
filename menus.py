from Menu import Menu
import themes
from actions import *

# MENUS
def mainmenu():
    menudict = {
               "+AUDIOMENU": audiomenu,
               "+HDMIMENU": hdmimenu,
               "NANI": video,
               "VIDEOS": videos,
               "BOOKS": books,
               "MANGAS": mangas,
               }
    Menu(menudict, 0, 0, "VCR.ttf", themes.theme1).run()


def hdmimenu():
    menudict = {
               "+PowerMenu": powermenu,
               "off+1920": hdmi1920,
               "1920+2560": hdmion,
               "1920+Off": hdmioff,
               }

    Menu(menudict, 0, 0, "VCR.ttf", themes.theme2).run()


def powermenu():
    menudict = {
               "MAIL": mail,
               "pavuContr0l": pavucontrol,
               }
    Menu(menudict, 0, 0, "VCR.ttf", themes.theme1).run()


def audiomenu():
    menudict = {
               "HDMIOUT": audiohdmi,
               "SPEADKEROUT": audiospeaker,
               "UP": volumeup,
               "DOWN": volumedown,
               "MUTE": mute,
               "PAVUCONTROL": pavucontrol,
               }

    Menu(menudict, 0, 0, "VCR.ttf", themes.theme2).run()
