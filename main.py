import pygame
from colour import Colour
from resolution import Resolution
from widgets import Button, Entry, Label, Multiple_Entry, Widget, TextBox, Checkbox
from window import Window

win = Window(Resolution(500, 500), "ALfie is shit at life")
but = Button(win, (50, 100)).place(0, 0)
win.mainloop()