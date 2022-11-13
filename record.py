import pygame

class Record:

    def __init__(self):
        self.records = []
    
    def check_event(self, event):
        self.records.append(event)

    def update(self):
        pass