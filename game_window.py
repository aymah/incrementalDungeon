import sys, pygame
from town_window import TownWindow

class GameWindow():

    def __init__(self):
        self.size = width, height = 1280, 720
        self.black = 0, 0, 0
        self.white = 255, 255, 255
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Incremental Dungeon')
        self.town_panel = TownWindow(0)


    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    sys.exit()

            # self.screen.fill(self.black)
            # self.town_panel.panel.fill(self.white)
            pygame.display.flip()
