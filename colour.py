class Colour:

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def get(self):
        self.checkValues()
        return (self.red, self.green, self.blue)

    def darken(self, amount):
        self.red *= amount
        self.green *= amount
        self.blue *= amount
        self.checkValues()

    def lighten(self, amount):
        self.red //= amount
        self.green //= amount
        self.blue //= amount
        self.checkValues()

    def checkValues(self):
        self.red = 255 if self.red > 255 else 0 if self.red < 0 else self.red
        self.green = 255 if self.green > 255 else 0 if self.green < 0 else self.green
        self.blue = 255 if self.blue > 255 else 0 if self.blue < 0 else self.blue