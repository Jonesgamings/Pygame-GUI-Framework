import pygame

class Font:

    def __init__(self, font, size, colour):
        self.font = pygame.font.SysFont(font, size)
        self.colour = colour
    
    def render(self, text):
        return self.font.render(text, False, self.colour.get())