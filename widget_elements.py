import pygame
from colour import Colour
from font import Font
import string

class Selectable:
    
    def __init__(self):
        self.selected_colour = Colour(200, 200, 200)
        self.rest_colour = self.colour

    def selectable_check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.collides(event.pos):
                    self.isSelected = True
                    self.onPress()

        if event.type == pygame.MOUSEBUTTONDOWN and self.isSelected and not self.collides(event.pos):
            self.isSelected = False
            self.colour = self.rest_colour
            self.onRelease()

        if self.isSelected:
            self.colour = self.selected_colour
            self.onSelected(event)

    def onSelected(self, event):
        pass

    def onRelease(self):
        pass

    def setSelectableColour(self, colour):
        self.selected_colour = colour

class StaySelectable:

    def __init__(self):
        self.selected_colour = Colour(200, 200, 200)
        self.rest_colour = self.colour

    def selectable_check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.collides(event.pos):
                    self.isSelected = not self.isSelected
                    self.onPress()

        if self.isSelected:
            self.colour = self.selected_colour
            self.onSelected(event)

        else:
            self.colour = self.rest_colour
            self.onRelease()

    def onSelected(self, event):
        pass

    def onRelease(self):
        pass

    def setSelectableColour(self, colour):
        self.selected_colour = colour

class Pressable:

    def __init__(self):
        self.selected_colour = Colour(200, 200, 200)
        self.rest_colour = self.colour

    def onPress(self):
        self.colour = self.selected_colour

    def onRelease(self):
        self.colour = self.rest_colour

    def onHold(self):
        pass

    def pressable_check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.collides(event.pos):
                    self.isSelected = True
                    self.onPress()

        if event.type == pygame.MOUSEBUTTONUP and self.isSelected:
            self.isSelected = False
            self.onRelease()

    def setRestColour(self, colour):
        self.rest_colour = colour

    def setSelectedColour(self, colour):
        self.selected_colour = colour

class Area:

    def __init__(self, size):
        self.x = 0
        self.y = 0
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.farX = self.x + self.width
        self.farY = self.y + self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.colour = None
        self.isSelected = False
        self.isShowing = True
        self.isPlaced = False

    def place(self, x, y):
        self.x = x
        self.y = y
        self.update()
        return self

    def collides(self, pos):
        if self.rect.collidepoint(pos):
            return True

        else:
            return False

    def update(self):
        self.farX = self.x + self.width
        self.farY = self.y + self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def blit(self, screen):
        pygame.draw.rect(screen, self.colour.get(), self.rect)

    def darken(self, amount):
        self.colour.darken(amount)

    def lighten(self, amount):
        self.colour.lighten(amount)

    def setColour(self, colour):
        self.colour = colour

    def move(self, x, y):
        self.x + x
        self.y + y
        self.update()

    def hide(self):
        self.isShowing = False
    
    def show(self):
        self.isShowing = True

    def setSize(self, size):
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.update()

class Border:

    def __init__(self):
        self.border_thickness = 1
        self.border_colour = Colour(0, 0, 0)

    def blit_border(self, screen):
        pygame.draw.rect(screen, self.border_colour.get(), self.rect, self.border_thickness)

    def setBorderThickness(self, thickness):
        self.thickness = thickness

    def setBorderColour(self, colour):
        self.border_colour = colour

class Text:

    def __init__(self):
        self.text = None
        self.text_colour = Colour(0, 0, 0)
        self.text_size = 15
        self.text_font = "Comic Sans MS"
        self.text_rend = Font(self.text_font, self.text_size, self.text_colour)
        self.text_x = 0
        self.text_y = 0

    def text_update(self):
        self.text_rend = Font(self.text_font, self.text_size, self.text_colour)
        
    def blit_text(self, screen):
        screen.blit(self.text_rend.render(self.text), (self.x + self.text_x, self.y + self.text_y))

    def setPos(self, x, y):
        self.text_x = x
        self.text_y = y
        self.text_update()
    
    def setFont(self, font):
        self.font = font
        self.text_update()

    def setTextSize(self, size):
        self.text_size = size
        self.text_update()

    def setTextColour(self, colour):
        self.text_colour = colour
        self.text_update()

    def setText(self, text):
        self.text = text
        self.text_update()

class Multiple_Text:

    def __init__(self):
        self.lines = []
        self.text_colour = Colour(0, 0, 0)
        self.text_size = 15
        self.text_font = "Comic Sans MS"
        self.text_rend = Font(self.text_font, self.text_size, self.text_colour)
        self.text_x = 0
        self.text_y = 0
        self.line_space = 30

    def multiple_text_update(self):
        self.text_rend = Font(self.text_font, self.text_size, self.text_colour)

    def blit_multiple_text(self, screen):
        for i, text in enumerate(self.lines):
            screen.blit(self.text_rend.render(text), (self.x + self.text_x, self.y + self.text_y + (self.line_space * i)))

    def text_update(self):
        self.text_rend = Font(self.text_font, self.text_size, self.text_colour)

    def setPos(self, x, y):
        self.text_x = x
        self.text_y = y
        self.text_update()
    
    def setFont(self, font):
        self.font = font
        self.text_update()

    def setTextSize(self, size):
        self.text_size = size
        self.text_update()

    def setTextColour(self, colour):
        self.text_colour = colour
        self.text_update()

    def setText(self, pos, text):
        self.lines[pos] = text
        self.text_update()

    def setLines(self, lines):
        self.lines = lines

    def setLineSpace(self, space):
        self.line_space = space
        self.text_update()

    def addText(self, text):
        self.lines.append(text)
        self.text_update()

class Input:

    def __init__(self):
        self.input_text = ""
        self.hidden_text = ""
        self.shownAs = None
        self.max_chars = 30
        self.caps = False

    def check_key(self, event):
        if event.type == pygame.KEYDOWN:
            key = event.key
            name = pygame.key.name(event.key)

            if key == pygame.K_LSHIFT or key == pygame.K_RSHIFT:
                self.caps = True

            elif key == pygame.K_BACKSPACE:
                if len(self.input_text) > 0:
                    self.input_text = self.input_text[:-1]
                    self.hidden_text = self.hidden_text[:-1]

            elif key == pygame.K_SPACE:
                self.input_text += " "
                self.hidden_text += self.shownAs if self.shownAs else ""

            elif name in string.printable:
                if len(self.input_text) + 1 <= self.max_chars: 
                    self.input_text += name if not self.caps else name.upper()
                    self.hidden_text += self.shownAs if self.shownAs else ""

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                self.caps = False

    def getInput(self):
        if not self.shownAs:
            return self.input_text

        else:
            return self.hidden_text

    def getRawInput(self):
        return self.input_text

    def setMaxCharacters(self, max):
        self.max_chars = max

    def setShownAs(self, showing):
        self.shownAs = showing

    def resetShwoing(self):
        self.shownAs = None

    def clearInput(self):
        self.input_text = ""
        self.hidden_text = ""

class Multiple_Input:

    def __init__(self):
        self.input_text = [""]
        self.hidden_text = [""]
        self.shownAs = None
        self.max_chars = 30
        self.max_lines = 5
        self.current_line = 0
        self.total_lines = 1
        self.caps = False

    def check_key(self, event):
        if event.type == pygame.KEYDOWN:
            key = event.key
            name = pygame.key.name(event.key)

            if key == pygame.K_LSHIFT or key == pygame.K_RSHIFT:
                self.caps = True

            elif key == pygame.K_RETURN:
                if self.total_lines + 1 != self.max_lines:
                    self.current_line += 1
                    self.input_text.insert(self.current_line, "")
                    self.hidden_text.insert(self.current_line, "")

            elif key == pygame.K_DOWN:
                if self.current_line + 1 != self.max_lines:
                    self.current_line += 1
                    if self.current_line == self.total_lines:
                        self.input_text.append("")
                        self.hidden_text.append("")
                        self.total_lines += 1

            elif key == pygame.K_UP:
                if self.current_line - 1 >= 0:
                    self.current_line -= 1
                    print(self.current_line) 

            elif key == pygame.K_BACKSPACE:
                if len(self.input_text[self.current_line]) > 0:
                    self.input_text[self.current_line] = self.input_text[self.current_line][:-1]
                    self.hidden_text[self.current_line] = self.hidden_text[self.current_line][:-1]

                else:
                    if self.current_line - 1 >= 0:
                        del self.input_text[self.current_line]
                        del self.hidden_text[self.current_line]
                        self.current_line -= 1

            elif key == pygame.K_SPACE:
                self.input_text[self.current_line] += " "
                self.hidden_text[self.current_line] += self.shownAs if self.shownAs else ""

            elif name in string.printable:
                if len(self.input_text) + 1 <= self.max_chars: 
                    self.input_text[self.current_line] += name if not self.caps else name.upper()
                    self.hidden_text[self.current_line] += self.shownAs if self.shownAs else ""

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                self.caps = False

    def getInput(self):
        if not self.shownAs:
            return self.input_text

        else:
            return self.hidden_text

    def getRawInput(self):
        return self.input_text

    def getLine(self, pos):
        if not self.shownAs:
            return self.input_text[pos]

        else:
            return self.hidden_text[pos]

    def getRawLine(self, pos):
        return self.input_text[pos]

    def setMaxCharacters(self, max):
        self.max_chars = max

    def setMaxLines(self, max):
        self.max_lines = max

    def setShownAs(self, showing):
        self.shownAs = showing

    def resetShwoing(self):
        self.shownAs = None

    def clearLines(self, line):
        self.input_text[line] = ""

    def clearInput(self):
        self.input_text = []
        self.hidden_text = []