from Menu import Menu
import themes
from actions import *
from subprocess import PIPE, check_output
import glob
import shlex

# MENUS
def mainmenu():
    menudict = {
               "+AUDIOMENU": 'audiomenu',
               "+HDMIMENU": hdmimenu,
               "IVIDEOS": ivideo,
               "InteractiveMenu": interactivemenu,
               }
    return Menu(menudict, 0, 0, "VCR.ttf", themes.pinky)


def hdmimenu():
    menudict = {
               "+PowerMenu": powermenu,
               "off+1920": hdmi1920,
               "1920+2560": hdmion,
               "1920+Off": hdmioff,
               }

    return Menu(menudict, 0, 0, "VCR.ttf", themes.black)


def powermenu():
    menudict = {
               "MAIL": mail,
               }
    return Menu(menudict, 0, 0, "VCR.ttf", themes.theme1)


def audiomenu():
    menudict = {
               "UP": volumeup,
               "DOWN": volumedown,
               "MUTE": mute,
               "PAVUCONTROL": pavucontrol,
               }

    return Menu(menudict, 0, 0, "VCR.ttf", themes.winky)


## INTERACTIVE MENU
# load bookmarks
# load files
# change audio output
# change video output

def interactivemenu():
    def getoptions():
        options = check_output(['ls','-1'])
        options = options.decode('utf-8').split('\n')[:-1]
        return options

    def command(arg):
        os.system(f"echo {arg} >> logs.txt")

    menudict = {}
    for o in getoptions():
        menudict[o] = (command, o)

    Menu(menudict, 0, 0, "VCR.ttf", themes.pinky).run()


def ivideo():
    def getoptions():
        home = os.path.expanduser('~')
        directory = os.path.join(home, 'Videos' , '*')
        options = glob.glob(directory)
        return options

    def command(arg):
        os.system(f"mpv '{arg}' &")

    menudict = {}
    for o in getoptions():
        menudict[o] = (command, o)

    Menu(menudict, 0, 0, "VCR.ttf", themes.banana).run()

