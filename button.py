class button:
    def __init__(self, label, x, y, txtcolor, bgcolor, bordercolor):
        self.label = label
        self.x = x
        self.y = y
        self.txtcolor = txtcolor
        self.bgcolor = bgcolor
        self.bordercolor = bordercolor


    def debug(self):
        print(self.label, self.x, self.y)


    def draw(self):
        pass


    def update(self):
        pass
