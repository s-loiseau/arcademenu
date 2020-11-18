# Textwrap
## for Popup, handle long text with textwrap module.
# Menus dynamic
## work on dir scanner or else to build a list of args, as button
## labels could be used as args for a specific command.
## should limit output length.
## Like:
```
menudyn = sxivmenu()


def sxiv(file):
    os.system('sxiv + file)


def sxivmenu():
    listfiles = os glob directory
    menudict = {}
    for f in listfiles:
        mendict[f] = (sxiv, f)
    return menudict
```

should modify action feature to handle tuples with args for functions.
