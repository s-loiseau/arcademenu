import os
import subprocess

# ACTIONS

## AUDIO
def pavucontrol():
    os.system("pavucontrol &")

def volumeup():
    os.system("setvolume.sh increase &")

def volumedown():
    os.system("setvolume.sh decrease &")

def mute():
    os.system("setvolume.sh mute &")


## VIDEO
def hdmi1920():
    os.system('xrandr --output HDMI-0 --mode 1920x1080 &')
    os.system("feh --randomize --bg-fill ~/Pictures/wallpaper/*")

def hdmi2560():
    os.system('xrandr --output HDMI-0 --mode 2560x1080 &')
    os.system("feh --randomize --bg-fill ~/Pictures/wallpaper/*")

## APPS
def terminal():
    os.system("urxvt &")

def mail():
    os.system("urxvt -geometry 80x40 -e bash -c 'neomutt' &")

def web():
    os.system("qutebrowser www.reddit.com/r/france/new &")

## POWER
def poweroff():
    os.system("poweroff")

## FUNNY
def video():
    os.system("mpv --really-quiet ~/Videos/joueurdugrenierrage.mp4 &")
