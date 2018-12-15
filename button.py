import pygame
from color import Color

class Button():

    def __init__(self, x, y, w, h, image1, image2, image3, action): #images = no interaction, hover, popup
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.action = action

    def clone(self, button):
        self.x = button.x
        self.y = button.y
        self.w = button.w
        self.h = button.h
        self.image1 = button.image1
        self.image2 = button.image2
        self.image3 = button.image3
        self.action = button.action


    def check_position(self, pos):
        width, height = pos
        if self.x <= width <= self.x + self.w and self.y <= height <= self.y + self.h:
            return True
        return False


    def draw(self, panel):
        mouse_pos = pygame.mouse.get_pos()
        image = self.image1
        if self.check_position(mouse_pos):
            image = self.image2
            popup_pos = self.x, self.y - self.image3.get_height()
            panel.blit (self.image3, popup_pos)
        pos = self.x, self.y
        panel.blit(image, pos)

    def execute_mouse_events(self):
        if self.action is not None:
            self.action()

    # def update(self, image1, image2, image3):

