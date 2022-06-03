import pygame
import settings


class Block:

    def __init__(self, color, size):
        self.color = color
        self.num = 0
        self.surface = pygame.Surface((size, size))
        self.font = pygame.font.SysFont(None, size)

    def update(self, new_num=None):
        if new_num is not None:
            self.num = new_num
        self.color = settings.BLOCK_COLORS[self.num]

    def draw(self, surface, pos):
        number = self.font.render(str(self.num),
                                  False,
                                  (settings.GAME_COLORS["Dark_number"] if self.num <= 4 else settings.GAME_COLORS["Light_number"]))
        self.surface.fill(settings.BLOCK_COLORS[self.num])
        sz = number.get_rect().size
        center = self.surface.get_rect().center
        cord = (center[0] - sz[0] // 2, center[1] - sz[1] // 2)
        if not self.empty():
            self.surface.blit(number, cord)
        surface.blit(self.surface, pos)

    def empty(self):
        return True if self.num == 0 else False
