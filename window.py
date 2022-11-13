from record import Record
from resolution import Resolution
from colour import Colour
from errors import PlaceError
import pygame

pygame.init()

class Window:

    def __init__(self, resolution: Resolution, name = "Main"):
        self.name: str = name
        self.height: int = None
        self.width: int = None
        self.resoltuion: Resolution = resolution
        self.screen = None
        self.children = []
        self.updating = False
        self.hasRecord = False

        self.background = Colour(255, 255, 255)

        self.init()

    def setResolution(self):
        self.width = self.resoltuion.witdh
        self.height = self.resoltuion.height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def init(self):
        self.setResolution()
        pygame.display.set_caption(self.name)

    def createRecord(self):
        self.children.append(Record())
        self.hasRecord = True

    def add(self, child_obj):
        self.children.append(child_obj)

    def getRecord(self):
        if self.hasRecord():
            return 

    def update(self):
        for child in self.children:
            child.update()

    def check_events(self, event):
        for child in self.children:
            child.check_event(event)

    def check_event(self, event):
        if event.type == pygame.QUIT:
            self.updating = False

    def mainloop(self):
        self.updating = True
        while self.updating:
            try:
                self.screen.fill(self.background.get())
                for event in pygame.event.get():
                    self.check_event(event)
                    self.check_events(event)
                
                self.update()

            except AttributeError as e:
                PlaceError(self, "Widget has not been placed on screen").raiseMe()
                print(e)

            pygame.display.flip()

        pygame.quit()

    def get(self):
        return self.screen

    def getWidth(self):
        return self.width