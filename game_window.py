import sys, pygame

class GameWindow():

    def _init_(self):
        self.size = width, height = 640, 480
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(size)
        # pygame.display.set_caption('Incremental Dungeon')


    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

            self.screen.fill(self.black)
            pygame.display.flip()