import pygame

class TownWindow():

    def __init__(self, depth):
        self.size = width, height = 640, 720
        self.position = width, height = 0, 0
        self.panel = pygame.Surface((self.size), depth + 1, None)
