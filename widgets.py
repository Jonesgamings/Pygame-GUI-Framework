import pygame
from widget_elements import Area, Border, Multiple_Input, Selectable, StaySelectable, Text, Input, Pressable, Multiple_Text
from font import Font
from colour import Colour

def OnPress():
    pass

def OnHold():
    pass

def OnRelease():
    pass

class Widget(Area, Border):

    def __init__(self, window, size):
        Area.__init__(self, size)
        Border.__init__(self)
        
        self.window = window
        self.background_colour = Colour(255, 255, 255)
        self.colour = self.background_colour
        self.init()

    def init(self):
        self.window.add(self)

    def blit(self, screen):
        super().blit(screen)
        super().blit_border(screen)

    def update(self):
        super().update()

        screen = self.window.get()
        if self.isShowing:
            self.blit(screen)
            if self.isSelected:
                self.onHold()

    def onPress(self):
        pass

    def onRelease(self):
        pass

    def onHold(self):
        pass

    def check_event(self, event):
        pass

class Label(Widget, Text):

    def __init__(self, window, size):
        super().__init__(window, size)
        Text.__init__(self)

    def blit(self, screen):
        super().blit(screen)
        super().blit_text(screen)

class Button(Label, Pressable):

    def __init__(self, window, size):
        Label.__init__(self, window, size)
        Pressable.__init__(self)

        self.press_cmd = OnPress
        self.hold_cmd = OnHold
        self.release_cmd = OnRelease
        self.selected_colour = Colour(200, 200, 200)
        self.rest_colour = self.colour

    def onPress(self):
        super().onPress()
        self.press_cmd()
        self.colour = self.selected_colour

    def onHold(self):
        super().onHold()
        self.hold_cmd()

    def onRelease(self):
        super().onRelease()
        self.release_cmd()
        self.colour = self.rest_colour

    def setPressCmd(self, cmd):
        self.press_cmd = cmd

    def setHoldCmd(self, cmd):
        self.hold_cmd = cmd

    def setRelease(self, cmd):
        self.release_cmd = cmd

    def setSelectedColour(self, colour):
        self.selected_colour = colour

    def check_event(self, event):
        super().pressable_check_event(event)

class TextBox(Widget, Multiple_Text):

    def __init__(self, window, size):
        super().__init__(window, size)
        Multiple_Text.__init__(self)

    def blit(self, screen):
        super().blit(screen)
        super().blit_multiple_text(screen)

class Entry(Label, Input, Selectable):

    def __init__(self, window, size):
        super().__init__(window, size)
        Input.__init__(self)
        Selectable.__init__(self)

    def onSelected(self, event):
        super().onSelected(event)
        self.check_key(event)
        self.setText(self.getInput())

    def clearInput(self):
        super().clearInput()
        self.setText(self.getInput())

    def check_event(self, event):
        super().selectable_check_event(event)

class Multiple_Entry(TextBox, Multiple_Input, Selectable):

    def __init__(self, window, size):
        super().__init__(window, size)
        Multiple_Input.__init__(self)
        Selectable.__init__(self)

    def onSelected(self, event):
        super().onSelected(event)
        self.check_key(event)
        self.setLines(self.getInput())

    def clearInput(self):
        super().clearInput()
        self.setLines(self.getInput())

    def check_event(self, event):
        super().selectable_check_event(event)

class Checkbox(Widget, StaySelectable):

    def __init__(self, window, size):
        super().__init__(window, size)
        Selectable.__init__(self)

    def check_event(self, event):
        super().selectable_check_event(event) 