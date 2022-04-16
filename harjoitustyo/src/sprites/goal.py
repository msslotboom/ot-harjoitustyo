import os
import pygame
dirname = os.path.dirname(__file__)


class Goal(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0) -> None:
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "ovi.png")
        )

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (pos_x, pos_y)
        self.width = self.rect[2]
        self.height = self.rect[3]
