import sys, pygame
from town_window import TownWindow
from color import Color
from game_settings import GameSettings

class GameWindow():

    def __init__(self):
        self.game_settings = GameSettings()
        self.size = width, height = self.game_settings.game_width, self.game_settings.game_height
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Incremental Dungeon')
        self.town_panel_wrapper = TownWindow(0)


    def run(self):
        last_refresh_time = last_update_time = pygame.time.get_ticks()
        while 1:
            if last_refresh_time + self.game_settings.refresh_time <= pygame.time.get_ticks():
                last_refresh_time += self.game_settings.refresh_time
                self.refresh_frame()
            if last_update_time + self.game_settings.update_time <= pygame.time.get_ticks():
                last_update_time += self.game_settings.update_time
                self.update_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    self.update_state()


    def refresh_frame(self):
        self.screen.fill(Color.white)
        self.town_panel_wrapper.refresh_frame()
        self.screen.blit(self.town_panel_wrapper.panel, self.town_panel_wrapper.position)
        pygame.display.flip()

    def update_state(self):
        self.town_panel_wrapper.update_state()