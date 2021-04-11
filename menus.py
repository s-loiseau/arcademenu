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
               "+HDMIMENU": 'hdmimenu',
               "IVIDEOS": 'ivideo',
               "InteractiveMenu": 'interactivemenu',
               }
    #return Menu(menudict, 0, 0, "VCR.ttf", themes.termgreen)
    return Menu(menudict, 0, 0, "VCR.ttf", themes.miami)


def hdmimenu():
    menudict = {
               "+PowerMenu": 'powermenu',
               "2560": hdmi2560,
               "1920": hdmi1920,
               "terminal": terminal
               }

    return Menu(menudict, 0, 0, "VCR.ttf", themes.banana1)


def powermenu():
    menudict = {
               "MAIL": mail,
               }
    return Menu(menudict, 0, 0, "VCR.ttf", themes.black)


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
        return None

    menudict = {}
    for o in getoptions():
        menudict[o] = (command, o)

    return Menu(menudict, 0, 0, "VCR.ttf", themes.winky)


def ivideo():
    def getoptions():
        home = os.path.expanduser('~')
        directory = os.path.join(home, 'Videos' , '**')
        options = glob.glob(directory, recursive=True)
        options = [o for o in options if o.endswith(('.mp4','.mkv'))]
        return sorted(options)

    def command(arg):
        os.system(f"mpv --geometry=30% '{arg}' &")

    menudict = {}
    print(getoptions())
    for o in getoptions():
        label = o.split(os.path.sep)[-1]
        menudict[label] = (command, o)

    return Menu(menudict, 0, 0, "VCR.ttf", themes.banana)

