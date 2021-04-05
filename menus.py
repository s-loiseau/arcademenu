from Menu import Menu
import themes
from actions import *
from subprocess import PIPE, check_output
import glob

# MENUS
def mainmenu():
    menudict = {
               "+AUDIOMENU": audiomenu,
               "+HDMIMENU": hdmimenu,
               "VIDEOS": videos,
               "IVIDEOS": ivideo,
               "InteractiveMenu": interactivemenu,
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
               }
    Menu(menudict, 0, 0, "VCR.ttf", themes.theme1).run()


def audiomenu():
    menudict = {
               "UP": volumeup,
               "DOWN": volumedown,
               "MUTE": mute,
               "PAVUCONTROL": pavucontrol,
               }

    Menu(menudict, 0, 0, "VCR.ttf", themes.theme2).run()


## INTERACTIVE MENU
# load bookmarks
# load files
# change audio output
# change video output

def interactivemenu():
    #template command
    def command():
        print(o)

    #list options
    #options = ["COCO", "TITI"]
    # get output of a command
    options = check_output(['ls','-1'])
    options = options.decode('utf-8').split('\n')[:-1]

    #build menudict
    menudict = {}
    for o in options:
        menudict[o] = command
    #call menu
    Menu(menudict, 0, 0, "VCR.ttf", themes.theme2).run()


def ivideo():
    #template command
    def command():
        #print(o)
        os.system('mpv ' + o + ' &')

    #list options
    # get output of a command
    home = os.path.expanduser('~')
    directory = os.path.join(home, 'Videos/*')
    options = glob.glob(directory)

    #build menudict
    menudict = {}
    for o in options:
        menudict[o] = command
    #call menu
    Menu(menudict, 0, 0, "VCR.ttf", themes.theme2).run()

