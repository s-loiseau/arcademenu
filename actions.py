import os
import subprocess

# ACTIONS

## AUDIO
def audiohdmi():
    os.system("pactl set-card-profile 0 output:hdmi-stereo-extra1+input:analog-stereo")

def audiospeaker():
    os.system("pactl set-card-profile 0 output:analog-stereo+input:analog-stereo")

def pavucontrol():
    os.system("pavucontrol &")

def volumeup():
    os.system("setvolume.sh increase &")

def volumedown():
    os.system("setvolume.sh decrease &")

def mute():
    os.system("setvolume.sh mute &")


## VIDEO
def hdmionly():
    os.system("~/.screenlayout/onlyhdmi2560.sh")
    os.system("feh --randomize --bg-fill ~/Pictures/wallpaper/*")


def hdmion():
    os.system("~/.screenlayout/1920hdmi2.sh")
    os.system("feh --randomize --bg-fill ~/Pictures/wallpaper/*")

def hdmioff():
    os.system("~/.screenlayout/nohdmi.sh")
    os.system("feh --randomize --bg-fill ~/Pictures/wallpaper/*")

def hdmi1920():
    os.system("~/.screenlayout/onlyhdmi19.sh")
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



