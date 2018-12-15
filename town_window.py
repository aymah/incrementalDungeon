import sys, pygame
from color import Color
from town_controller import TownController
from town import Town
from button import Button

class TownWindow():



    def __init__(self, depth, game_settings):
        self.game_settings = game_settings 
        self.size = width, height = 640, 720
        self.position = width, height = 0, 0
        self.depth = depth + 1
        self.panel = pygame.Surface((self.size), self.depth, None)
        self.town_controller = TownController()
        self.town = self.town_controller.town
        self.buttons = self._create_buttons()
        self.dungeon_window = None

    def _create_buttons(self):
        buttons = {}
        for y, building in enumerate(self.town.buildings.values()):
            button = self._create_button(building, y)
            buttons[building.name + " Add"] = button
            building.button = button
            building.needs_update = False
        return buttons

    def _create_button(self, building, y):
        font = self.game_settings.helvetica10

        text = building.name + ": " + str(building.number)
        text_surface = font.render(text, True, Color.white, None)

        text_surface_popup = self._build_cost_popup(building)
        text_surface_active = font.render(text, True, Color.green, None)

        w = text_surface.get_width()
        h = text_surface.get_height()
        return Button(50, 350 + 15 * y, w, h, text_surface, text_surface_active, text_surface_popup, lambda: building.build(self.town))

    def execute_mouse_events(self, pos):
        if self.check_position(pos):
            for button_name, button in self.buttons.items():
                if button.check_position(pos):
                    button.execute_mouse_events()

    def check_position(self, pos):
        width, height = pos
        if self.position[0] <= width <= self.position[0] + self.size[0] and self.position[1] <= height <= self.position[1] + self.size[1]:
            return True
        return False

    def refresh_frame(self):
        self._draw_bg()
        self._draw_text()

    def _draw_bg(self):
        self.panel.fill(Color.black)

    def _draw_text(self):
        self._check_for_updates()
        self._draw_resources()
        self._draw_equipment()
        self._draw_buttons()
        self._draw_next_party()

    def _check_for_updates(self):
        for y, building in enumerate(self.town.buildings.values()):
            if building.needs_update:
                building.button.clone(self._create_button(building, y))
                building.needs_update = False

    def _draw_resources(self):
        y = 0
        for resource, amount in self.town.resources.items():
            text = resource + ": " + str(amount)
            text_surface = self.game_settings.helvetica10.render(text, True, Color.white, None)
            text_position = width, height = 50, 50 + 15 * y
            self.panel.blit(text_surface, text_position)
            y += 1

    def _draw_equipment(self):
        y = 0
        for name, amount in self.town.equipment.items():
            text = name + ": " + str(amount)
            text_surface = self.game_settings.helvetica10.render(text, True, Color.white, None)
            text_position = width, height = 200, 50 + 15 * y
            self.panel.blit(text_surface, text_position)

            item = self.town.weapons[name]
            text = str(item.craft_progress) + "/" + str(item.craft_time)
            text_surface = self.game_settings.helvetica10.render(text, True, Color.white, None)
            text_position = width, height = 325, 50 + 15 * y
            self.panel.blit(text_surface, text_position)
            y += 1



    def _draw_buttons(self):
        for button_name, button in self.buttons.items():
            button.draw(self.panel)


    def _build_cost_popup(self, building):
        font = self.game_settings.helvetica10
        size = w, h = 100, 8 + len(building.cost) * 15
        surface = pygame.Surface(size, self.depth + 1, None)
        surface.fill(Color.white)
        y = 0
        for resource, amount in building.cost.items():
            text = resource + ": " + str(amount)
            text_position = 5, 5 + 15 * y
            text_surface = font.render(text, True, Color.black, None)
            surface.blit(text_surface, text_position)
            y += 1

        return surface

    def _draw_next_party(self):
        party = self.town.parties.popleft()
        self.town.parties.appendleft(party)
        if party is not None:
            name_text = party.adventurers[0].name
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.white, None)
            name_text_position = width, height = 400, 50
            self.panel.blit(name_text_surface, name_text_position)
            class_name = ""
            if party.adventurers[0].heroic:
                class_name += "Heroic "
            class_name += str(party.adventurers[0].adventurer_class.name)
            name_text =  "Class: " + class_name
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.white, None)
            name_text_position = width, height = 400, 65
            self.panel.blit(name_text_surface, name_text_position)
            name_text =  "Level: " + str(party.adventurers[0].level)
            name_text_surface = self.game_settings.helvetica10.render(name_text, True, Color.white, None)
            name_text_position = width, height = 400, 80
            self.panel.blit(name_text_surface, name_text_position)
            hp_text = "HP:   " + str(party.adventurers[0].curr_hp) + "/" + str(party.adventurers[0].max_hp)
            hp_text_surface = self.game_settings.helvetica10.render(hp_text, True, Color.white, None)
            hp_text_position = width, height = 400, 95
            self.panel.blit(hp_text_surface, hp_text_position)
            str_text = "STR:  " + str(party.adventurers[0].str)
            str_text_surface = self.game_settings.helvetica10.render(str_text, True, Color.white, None)
            str_text_position = width, height = 400, 110
            self.panel.blit(str_text_surface, str_text_position)
            str_text = "Weapon:  " + str(party.adventurers[0].weapon.name)
            str_text_surface = self.game_settings.helvetica10.render(str_text, True, Color.white, None)
            str_text_position = width, height = 400, 125
            self.panel.blit(str_text_surface, str_text_position)
            str_text = "EHP:  " + str(party.adventurers[0].get_ehp())
            str_text_surface = self.game_settings.helvetica10.render(str_text, True, Color.white, None)
            str_text_position = width, height = 400, 140
            self.panel.blit(str_text_surface, str_text_position)
            str_text = "DPS:  " + str(party.adventurers[0].get_dps())
            str_text_surface = self.game_settings.helvetica10.render(str_text, True, Color.white, None)
            str_text_position = width, height = 400, 155
            self.panel.blit(str_text_surface, str_text_position)

        else:
            text = "There are no parties at this time"
            text_surface = self.game_settings.helvetica10.render(text, True, Color.white, None)
            text_position = width, height = 400, 50
            self.panel.blit(text_surface, text_position)


    def update_state(self): #could add timescale to this function for multiple seconds?
        self.town_controller.update_state(self.dungeon_window)
