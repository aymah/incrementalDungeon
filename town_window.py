import pygame
from color import Color
from town_controller import TownController
from town import Town

class TownWindow():



    def __init__(self, depth):
        self.size = width, height = 640, 720
        self.position = width, height = 0, 0
        self.panel = pygame.Surface((self.size), depth + 1, None)
        self.town_controller = TownController()
        self.town = self.town_controller.town

    def refresh_frame(self):
        self._draw_bg()
        self._draw_text()

    def _draw_bg(self):
        self.panel.fill(Color.black)

    def _draw_text(self):
        helvetica10 = pygame.font.SysFont("helvetica", 10)
        text = "Gold: " + str(self.town.gold)
        text_surface = helvetica10.render(text, True, Color.white, None)
        text_position = width, height = 50, 50
        self.panel.blit(text_surface, text_position)

    def update_state(self): #could add timescale to this function for multiple seconds?
        self.town_controller.update_state()
