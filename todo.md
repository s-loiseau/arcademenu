# Bug Menu Height
shouldbe:
    v.border
    b.h = ( padding + texth + padding )
    vmargin
    b.h = ( padding + texth + padding )
    vmargin
    b.h = ( padding + texth + padding )
    vmargin
    b.h = ( padding + texth + padding )
    v.border

# ACTIONS
actions

# fx
blink
sounds

# Maze class
menu instanciates buttons
menu draw buttons
menu select next prev
menu enter

# Actions
improve mapping actions
menusdict
   V
actionsdict
   V
actions functions



## menudictexample:

""" menus.py """
def functionname():
    print("coco")

def submenu1():
    menu(submenudict)

menudict = {"label1": functionname,
            "label2": functionname,
            "label4": functionname,
            "label3": functionname,
           }

---

""" menu.py """
class menu():
    def __init__(menudict):
        buttonlist = menudict.keys()
        self.active = True
        b.action = menudict[b.name]

    def buttonaction(self):
        menudict['label']()
    
    def run(self):
        while self.active:
            update()
            draw()
    def quit(self):
        self.active = False
---
