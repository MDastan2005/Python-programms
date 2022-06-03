import pygame
from Table import Table
import settings


class Game:
    window = pygame.display.set_mode(settings.WINDOW_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Game 2048")
    pygame.init()

    def __init__(self):
        self.table = Table((4, 4), 125)
        self.game_running = 1
        self.FPS = 1

    def run(self):
        self.table.update()
        self.table.update()
        while self.game_running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = 0
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.table.update(3)
                    elif event.key == pygame.K_RIGHT:
                        self.table.update(1)
                    elif event.key == pygame.K_DOWN:
                        self.table.update(2)
                    elif event.key == pygame.K_UP:
                        self.table.update(0)
            self.draw()

    def draw(self):
        self.table.draw(self.window)
        pygame.display.flip()

    def update(self):
        pass
