import os
import pygame
dirname = os.path.dirname(__file__)


class Barrier(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos_x, pos_y
