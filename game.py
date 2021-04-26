import pygame
from client import *

class Game(Client):
    def __init__(self, ip, port, login):
        self.login = login
        super().__init__(ip, port, login)

        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))

    def _update(self):
        events = pygame.event.get()
        for event in events :
            if event.type == pygame.QUIT :
                self.running = False
        #self.entities.updateall()
        self.entities.updateMe(self.login, "Player", events)

    def _draw(self):
        self.screen.fill(0)
        self.entities.drawAll(self.screen)
        pygame.display.flip()

    def run(self):
        print("Running")
        while self.running :
            super().frameBegin()
            self._update()
            self._draw()
            super().frameEnd()
        quit()

gm = Game(sys.argv[1], sys.argv[2], sys.argv[3])
gm.run()