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
        for equip, amount in self.town.equipment.items():
            if equip.craft_time > 0:
                name = equip.name
                text = name + ": " + str(amount)
                text_surface = self.game_settings.helvetica10.render(text, True, Color.white, None)
                text_position = width, height = 200, 50 + 15 * y
                self.panel.blit(text_surface, text_position)

                text = str(equip.craft_progress) + "/" + str(equip.craft_time)
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
        text_color = Color.white
        x = 400
        y = 50
        y_inc = 15
        if party is not None:
            adventurer = party.adventurers[0]
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
            text_list.append("Abilities:")
            for ability in adventurer.get_abilities():
                text_list.append("               " + ability.name)
            self._draw_text_list(text_list, x, y, 0, y_inc, text_color)
        else:
            self._draw_text_item("There are no parties at this time", x, y, text_color)

    def _draw_text_list(self, text_list, x, y, x_inc, y_inc, text_color):
        for text in text_list:
            self._draw_text_item(text, x, y, text_color)
            x += x_inc
            y += y_inc

    def _draw_text_item(self, text, x, y, text_color):
        text_surface = self.game_settings.helvetica10.render(text, True, text_color, None)
        text_position = x, y
        self.panel.blit(text_surface, text_position)

    def update_state(self): #could add timescale to this function for multiple seconds?
        self.town_controller.update_state(self.dungeon_window)
