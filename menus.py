from Menu import Menu
import os
import themes

"""
 bindsym $mod+Return           exec urxvt -geometry 80x40

 rofi -show run
 thunar
 /usr/bin/python /home/krao/Code/pygame/exoclass/main.py
 feh --randomize --bg-fill ~/Pictures/wallpaper/*

 showb.sh
 showv.sh
 clock.sh
 getbattery.sh
 brii.sh -100
 brii.sh 100
 touchpadtoggle.sh
 wifi
 # return data function
 locker.sh
"""
"""
mainmenu
  +video
    hdmionly
    hdmionly1920
    hdmioff
  +audio
    selectoutput
    volume up
    volume down
    mute
    radio
  +power
    powerdown
  +network
    scan nmap
"""

# ACTIONS

## AUDIO
def pavucontrol():
    os.system("pavucontrol &")

def volumeup():
    os.system("setvolume.sh increase")

def volumedown():
    os.system("setvolume.sh decrease")

def mute():
    os.system("setvolume.sh mute")

## VIDEO
def hdmionly():
    os.system("~/.screenlayout/onlyhdmi19.sh")


def hdmi():
    os.system("~/.screenlayout/1920hdmi2.sh")

## APPS
def terminal():
    os.system("urxvt &")
def mail():
    os.system("urxvt -geometry 80x40 -e bash -c 'mutt' &")
def web():
    os.system("qutebrowser www.reddit.com/r/france/new &")

## POWER
def poweroff():
    os.system("poweroff")

## FUNNY
def video():
    os.system("mpv --really-quiet /home/krao/Videos/joueurdugrenierrage.mp4 &")


# MENUS
def mainmenu():
    Menu(mainmenudict, 0, 0, "VCR.ttf", themes.theme2).run()

def hdmimenu():
    Menu(hdmimenudict, 0, 0, "VCR.ttf", themes.theme2).run()


def powermenu():
    Menu(powermenudict, 0, 0, "katakana tfb.ttf", themes.theme1).run()

def audiomenu():
    Menu(audiomenudict, 0, 0, "hiragana tfb.ttf", themes.theme1).run()



mainmenudict = {
           "+AUDIOMENU": audiomenu,
           "+POWERMENU": powermenu,
           "+HDMIMENU": hdmimenu,
           }


powermenudict = {
           "WEB": mainmenu,
           "MAIL": mail,
           "POWEROFF": pavucontrol,
           }


hdmimenudict = {
           "0ff+2560": hdmionly,
           "off+1920": hdmi,
           "1920+2560": hdmi,
           "1920+1920": hdmi,
           }


audiomenudict = {
           "PAVUCONTROL": pavucontrol,
           "UP": volumeup,
           "DOWN": volumedown,
           "MUTE": mute,
           }

