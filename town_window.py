import pygame
from color import Color

class TownWindow():

    def __init__(self, depth):
        self.size = width, height = 640, 720
        self.position = width, height = 0, 0
        self.panel = pygame.Surface((self.size), depth + 1, None)

    def draw_bg(self):
    	self.panel.fill(Color.black)

    def draw_text(self):
    	helvetica10 = pygame.font.SysFont("helvetica", 10)
    	text = "This is a test"
    	text_surface = helvetica10.render(text, True, Color.white, None)
    	text_position = width, height = 50, 50
    	self.panel.blit(text_surface, text_position)
