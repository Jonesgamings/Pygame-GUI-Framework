import pygame

pygame.init()

class Resolution:
    
    def __init__(self, width, height):
        self.witdh = width
        self.height = height
    
    @classmethod
    def getCurrentResolution(cls):
        monitor_info = pygame.display.Info()
        width = monitor_info.current_w
        height = monitor_info.current_h
        return Resolution(width, height)