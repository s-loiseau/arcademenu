from Menu import Menu
from Popup import Popup
import os
import themes

"""
 bindsym $mod+Return           exec urxvt -geometry 80x40

 rofi -show run
 thunar

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
def popup():
    obj = Popup("GROSSE DATA", "VCR.ttf")
    obj.run()

## AUDIO
"""
if [ $status_hdmi -eq 1 ];then
    # TURN OFF HDMI VIDEO OUTPUT
    xrandr --output HDMI-2 --off
    # SWITCH TO SPEAKER
    pactl set-card-profile 0 output:analog-stereo+input:analog-stereo
    message='SPEAKER'
elif [ $status_speaker -eq 1 ]; then
    # TURN ON HDMI VIDEO OUTPUT
    xrandr --output HDMI-2 --auto
    # SWITCH TO HDMI AUDIO
    pactl set-card-profile 0 output:hdmi-stereo-extra1+input:analog-stereo
    message='HDMI'
fi
"""

def audiohdmi():
    os.system("pactl set-card-profile 0 output:hdmi-stereo-extra1+input:analog-stereo")

def audiospeaker():
    os.system("pactl set-card-profile 0 output:analog-stereo+input:analog-stereo")

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
    os.system("feh --randomize --bg-fill ~/Pictures/wallpaper/*")


def hdmi():
    os.system("~/.screenlayout/1920hdmi2.sh")
    os.system("feh --randomize --bg-fill ~/Pictures/wallpaper/*")

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
    os.system("mpv --really-quiet ~/Videos/joueurdugrenierrage.mp4 &")


# MENUS
def mainmenu():
    Menu(mainmenudict, 0, 0, "VCR.ttf", themes.theme1).run()

def hdmimenu():
    Menu(hdmimenudict, 0, 0, "VCR.ttf", themes.theme2).run()


def powermenu():
    Menu(powermenudict, 0, 0, "VCR.ttf", themes.theme1).run()

def audiomenu():
    Menu(audiomenudict, 0, 0, "VCR.ttf", themes.theme2).run()



mainmenudict = {
           "+AUDIOMENU": audiomenu,
           "+POWERMENU": powermenu,
           "+HDMIMENU": hdmimenu,
           "NANI": video,
           "popup": popup,
           }


powermenudict = {
           "WEB": mainmenu,
           "MAIL": mail,
           "pavuContr0l": pavucontrol,
           }


hdmimenudict = {
           "0ff+2560": hdmionly,
           "off+1920": hdmi,
           "1920+2560": hdmi,
           "1920+1920": hdmi,
           }


audiomenudict = {
           "HDMIOUT": audiohdmi,
           "SPEADKEROUT": audiospeaker,
           "UP": volumeup,
           "DOWN": volumedown,
           "MUTE": mute,
           "PAVUCONTROL": pavucontrol,
           }

