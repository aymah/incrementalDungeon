import pygame
from color import Color
from town_controller import TownController
from town import Town

class TownWindow():



    def __init__(self, depth, game_settings):
        self.game_settings = game_settings 
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
        self._draw_resources()
        self._draw_buildings()
        self._draw_next_party()


    def _draw_resources(self):
        y = 0
        for resource, amount in self.town.resources.items():
            text = resource + ": " + str(amount)
            text_surface = self.game_settings.helvetica10.render(text, True, Color.white, None)
            text_position = width, height = 50, 50 + 15 * y
            self.panel.blit(text_surface, text_position)
            y += 1


    def _draw_buildings(self):
        y = 0
        for building in self.town.buildings:
            text = building.name + ": " + str(building.cost["Gold"])
            text_surface = self.game_settings.helvetica10.render(text, True, Color.white, None)
            text_position = width, height = 50, 350 + 15 * y
            self.panel.blit(text_surface, text_position)
            y += 1

    def _draw_next_party(self):
        party = self.town.parties.popleft()
        self.town.parties.appendleft(party)
        if party is not None:
            name_text = party.adventurers[0].name
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.white, None)
            name_text_position = width, height = 350, 50
            self.panel.blit(name_text_surface, name_text_position)
            name_text =  "Level: " + str(party.adventurers[0].level)
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.white, None)
            name_text_position = width, height = 350, 65
            self.panel.blit(name_text_surface, name_text_position)
            hp_text = "HP:   " + str(party.adventurers[0].curr_hp) + "/" + str(party.adventurers[0].max_hp)
            hp_text_surface = self.game_settings.helvetica10.render(hp_text, True, Color.white, None)
            hp_text_position = width, height = 350, 80
            self.panel.blit(hp_text_surface, hp_text_position)
            str_text = "STR:  " + str(party.adventurers[0].str)
            str_text_surface = self.game_settings.helvetica10.render(str_text, True, Color.white, None)
            str_text_position = width, height = 350, 95
            self.panel.blit(str_text_surface, str_text_position)
        else:
            text = "There are no parties at this time"
            text_surface = self.game_settings.helvetica10.render(text, True, Color.white, None)
            text_position = width, height = 350, 50
            self.panel.blit(text_surface, text_position)


    def update_state(self): #could add timescale to this function for multiple seconds?
        self.town_controller.update_state()
