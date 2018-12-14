import pygame
from color import Color
from dungeon_controller import DungeonController
from dungeon import Dungeon

class DungeonWindow():



    def __init__(self, depth, game_settings, town_window):
        self.game_settings = game_settings
        self.size = width, height = 640, 720
        self.position = width, height = 640, 0
        self.panel = pygame.Surface((self.size), depth + 1, None)
        self.town_window = town_window
        self.dungeon_controller = DungeonController(self.town_window)
        self.dungeon = self.dungeon_controller.dungeon

    def refresh_frame(self):
        self._draw_bg()
        self._draw_text()

    def _draw_bg(self):
        self.panel.fill(Color.white)

    def _draw_text(self):
        self._draw_party()
        self._draw_monster()
        self._draw_misc()

    def _draw_party(self):
        party = self.dungeon.curr_party
        if party is not None:
            name_text = party.adventurers[0].name
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.black, None)
            name_text_position = width, height = 50, 50
            self.panel.blit(name_text_surface, name_text_position)
            name_text =  "Level: " + str(party.adventurers[0].level)
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.black, None)
            name_text_position = width, height = 50, 65
            self.panel.blit(name_text_surface, name_text_position)
            hp_text = "HP:   " + str(party.adventurers[0].curr_hp) + "/" + str(party.adventurers[0].max_hp)
            hp_text_surface = self.game_settings.helvetica10.render(hp_text, True, Color.black, None)
            hp_text_position = width, height = 50, 80
            self.panel.blit(hp_text_surface, hp_text_position)
            str_text = "STR:  " + str(party.adventurers[0].str)
            str_text_surface = self.game_settings.helvetica10.render(str_text, True, Color.black, None)
            str_text_position = width, height = 50, 95
            self.panel.blit(str_text_surface, str_text_position)
        else:
            text = "There are no parties at this time"
            text_surface = self.game_settings.helvetica10.render(text, True, Color.black, None)
            text_position = width, height = 50, 50
            self.panel.blit(text_surface, text_position)


    def _draw_monster(self):
        monster = self.dungeon.curr_monster
        if monster is not None:
            name_text = monster.name
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.black, None)
            name_text_position = width, height = 300, 50
            self.panel.blit(name_text_surface, name_text_position)
            name_text = "Level: " + str(monster.level)
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.black, None)
            name_text_position = width, height = 300, 65
            self.panel.blit(name_text_surface, name_text_position)
            hp_text = "HP:   " + str(monster.curr_hp) + "/" + str(monster.max_hp)
            hp_text_surface = self.game_settings.helvetica10.render(hp_text, True, Color.black, None)
            hp_text_position = width, height = 300, 80
            self.panel.blit(hp_text_surface, hp_text_position)
            str_text = "STR:  " + str(monster.str)
            str_text_surface = self.game_settings.helvetica10.render(str_text, True, Color.black, None)
            str_text_position = width, height = 300, 95
            self.panel.blit(str_text_surface, str_text_position)
        else:
            text = "There are no monsters at this time"
            text_surface = self.game_settings.helvetica10.render(text, True, Color.black, None)
            text_position = width, height = 300, 50
            self.panel.blit(text_surface, text_position)

    def _draw_misc(self):
        text = "Current Monsters Killed: " + str(self.dungeon.monsters_killed) + " monsters killed"
        text_surface = self.game_settings.helvetica10.render(text, True, Color.black, None)
        text_position = width, height = 50, 600
        self.panel.blit(text_surface, text_position)
        text = "Strongest Adventurer: " + str(self.dungeon.most_monsters_killed) + " monsters killed"
        text_surface = self.game_settings.helvetica10.render(text, True, Color.black, None)
        text_position = width, height = 300, 600
        self.panel.blit(text_surface, text_position)

    def update_state(self): #could add timescale to this function for multiple seconds?
        self.dungeon_controller.update_state()
