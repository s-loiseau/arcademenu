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
 locker.sh
 setvolume.sh decrease
 setvolume.sh increase
 setvolume.sh mute
 brii.sh -100
 brii.sh 100
 touchpadtoggle.sh
"""


def video():
    os.system("mpv --really-quiet /home/krao/Videos/joueurdugrenierrage.mp4 &")


def terminal():
    os.system("urxvt &")


def hdmionly():
    os.system("~/.screenlayout/onlyhdmi19.sh")


def hdmi():
    os.system("~/.screenlayout/1920hdmi2.sh")



def mail():
    os.system("urxvt -geometry 80x40 -e bash -c 'mutt' &")



def pavucontrol():
    os.system("pavucontrol &")


def web():
    os.system("qutebrowser www.reddit.com/r/france/new &")


def poweroff():
    os.system("poweroff")


def hdmimenu():
    Menu(menu1, 0, 0, "VCR.ttf", themes.theme1).run()


def powermenu():
    Menu(menu2, 0, 0, "katakana tfb.ttf", themes.theme2).run()

def audiomenu():
    Menu(menu3, 0, 0, "VCR.ttf", themes.theme2).run()



menu1 = {
           "AUDIOMENU": audiomenu,
           "POWERMENU": powermenu,
           "AUDIO": pavucontrol,
           }


menu2 = {
           "WEB": web,
           "MAIL": mail,
           "DSFDFLKJ": pavucontrol,
           }

menu3 = {
           "AUDIO": pavucontrol,
           "DFSDF": powermenu,
           }

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
