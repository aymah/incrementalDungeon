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
        self.town_window.dungeon_window = self

    def execute_mouse_events(self, pos):
        if self.check_position(pos):
            self.update_state()
            # for button_name, button in self.buttons.items():
            #     if button.check_position(pos):
            #         button.execute_mouse_events()

    def check_position(self, pos):
        width, height = pos
        if self.position[0] <= width <= self.position[0] + self.size[0] and self.position[1] <= height <= self.position[1] + self.size[1]:
            return True
        return False

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
        text_color = Color.black
        x = 50
        y = 50
        y_inc = 15
        if party is not None:
            self._draw_adventurer(x, y, 0, y_inc, text_color, party.adventurers[0])
        else:
            self._draw_text_item("There are no parties at this time", x, y, text_color)

    def _draw_adventurer(self, x, y, x_inc, y_inc, text_color, adventurer):
            text_list = []
            text_list.append(adventurer.name)
            class_name = ""
            if adventurer.heroic:
                class_name += "Heroic "
            class_name += str(adventurer.adventurer_class.name)
            text_list.append("Class: " + class_name)
            text_list.append("Level: " + str(adventurer.level))
            text_list.append("HP:   " + str(adventurer.curr_hp) + "/" + str(adventurer.max_hp))
            text_list.append("STR:  " + str(adventurer.str))
            for slot, equip in adventurer.equipment.items():
                text_list.append(slot + ":  " + str(equip.name))
            text_list.append("EHP:  " + str(adventurer.get_ehp()))
            text_list.append("DPS:  " + str(adventurer.get_dps()))
            text_list.append("Monsters Killed:  " + str(adventurer.monsters_killed))
            text_list.append("Gold Earned:  " + str(adventurer.gold_earned))
            text_list.append("Time Survived:  " + str(adventurer.time))

            self._draw_text_list(text_list, x, y, 0, y_inc, text_color)

    def _draw_text_list(self, text_list, x, y, x_inc, y_inc, text_color):
        for text in text_list:
            self._draw_text_item(text, x, y, text_color)
            x += x_inc
            y += y_inc

    def _draw_text_item(self, text, x, y, text_color):
        text_surface = self.game_settings.helvetica10.render(text, True, text_color, None)
        text_position = x, y
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
        text_color = Color.black
        self._draw_text_item("Last Adventurer:", 50, 500, text_color)
        if self.dungeon.last_adventurer is not None:
            self._draw_adventurer(50, 515, 0, 15, text_color, self.dungeon.last_adventurer)
        else:
            self._draw_text_item("No Last Adventurer", 50, 515, text_color)
        self._draw_text_item("Greatest Adventurer:", 300, 500, text_color)
        if self.dungeon.greatest_adventurer is not None:
            self._draw_adventurer(300, 515, 0, 15, text_color, self.dungeon.greatest_adventurer)
        else:
            self._draw_text_item("No Greatest Adventurer", 300, 515, text_color)
        last_attack = self.dungeon_controller.get_last_attack()
        self._draw_text_item("Last Move:", 50, 350, text_color)
        if last_attack is not None:
            self._draw_text_item(last_attack["Attacker"].name + " attacked " + last_attack["Defender"].name + " with " + last_attack["Ability"].name + " dealing " + str(last_attack["Damage"]) + " damage.", 50, 365, text_color)
        else:    
            self._draw_text_item("No Last Move", 50, 365, text_color)
    def update_state(self): #could add timescale to this function for multiple seconds?
        self.dungeon_controller.update_state()
