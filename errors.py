class Error:

    def __init__(self, win, name, reason):
        self.win = win
        self.name = name
        self.reason = reason

    def raiseMe(self):
        print("{0}: {1}".format(self.name, self.reason))
        self.win.updating = False

class PlaceError(Error):
    def __init__(self, win, reason):
        super().__init__(win, "PlaceError", reason)