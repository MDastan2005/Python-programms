import settings
import pygame
from Block import Block
import random


class Table:

    def __init__(self, block_num, block_size):
        self.size = block_num
        self.block_size = block_size
        self.arr = [[Block(settings.BLOCK_COLORS[0], block_size) for _ in range(self.size[1])] for _ in range(self.size[0])]
        self.surface = pygame.Surface(settings.WINDOW_SIZE)

    def draw(self, surface):
        self.surface.fill(settings.GAME_COLORS["Back_ground"])
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.arr[i][j].draw(self.surface, self._blocks_drawing_cor((i, j)))
        surface.blit(self.surface, (0, 0))

    def _blocks_drawing_cor(self, pos):
        y, x = pos
        return (x + 1) * settings.INDENT + x * self.block_size, (y + 1) * settings.INDENT + y * self.block_size

    def _get_random_block(self):
        free_blocks = []
        for a in self.arr:
            for block in a:
                if block.empty():
                    free_blocks.append(block)
        return random.choice(free_blocks)

    def _choose_set_number(self):
        block = self._get_random_block()
        probability = random.random()
        if probability <= 0.1:
            block.update(4)
        else:
            block.update(2)

    def rotate(self, direction):
        if direction == 0:
            for j in range(self.size[1]):
                pos = 0
                new = []
                for i in range(self.size[0]):
                    cur = self.arr[i][j]
                    if not cur.empty():
                        new.append(cur.num)
                        pos += 1
                for i in range(len(new) - 1, 0, -1):
                    if new[i] == new[i - 1]:
                        new[i - 1] *= 2
                for i in range(self.size[0]):
                    if i < len(new):
                        self.arr[i][j].update(new[i])
                    else:
                        self.arr[i][j].update(0)
            return
        elif direction == 1:
            for i in range(self.size[0]):
                pos = self.size[1] - 1
                new = []
                for j in range(self.size[1] - 1, -1, -1):
                    cur = self.arr[i][j]
                    if not cur.empty():
                        new.append(cur.num)
                        pos -= 1
                for j in range(len(new) - 1, 0, -1):
                    if new[j] == new[j - 1]:
                        new[j - 1] *= 2
                for j in range(self.size[1] - 1, -1, -1):
                    if self.size[1] - j - 1 < len(new):
                        self.arr[i][j].update(new[self.size[1] - j - 1])
                    else:
                        self.arr[i][j].update(0)
            return
        elif direction == 2:
            for j in range(self.size[1]):
                pos = self.size[0] - 1
                new = []
                for i in range(self.size[0] - 1, -1, -1):
                    cur = self.arr[i][j]
                    if not cur.empty():
                        new.append(cur.num)
                        pos -= 1
                for i in range(len(new) - 1, 0, -1):
                    if new[i] == new[i - 1]:
                        new[i - 1] *= 2
                for i in range(self.size[1] - 1, -1, -1):
                    if self.size[0] - i - 1 < len(new):
                        self.arr[i][j].update(new[self.size[0] - i - 1])
                    else:
                        self.arr[i][j].update(0)
            return
        elif direction == 3:
            for i in range(self.size[0]):
                pos = 0
                new = []
                for j in range(self.size[1]):
                    cur = self.arr[i][j]
                    if not cur.empty():
                        new.append(cur.num)
                        pos += 1
                for j in range(len(new) - 1, 0, -1):
                    if new[j] == new[j - 1]:
                        new[j - 1] *= 2
                for j in range(self.size[1]):
                    if j < len(new):
                        self.arr[i][j].update(new[j])
                    else:
                        self.arr[i][j].update(0)
            return

    def update(self, direction=None):
        if direction is not None:
            self.rotate(direction)
        self._choose_set_number()
