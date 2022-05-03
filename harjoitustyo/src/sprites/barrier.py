import os
import pygame
dirname = os.path.dirname(__file__)


class Barrier(pygame.sprite.Sprite):
    """Luokka joka tekee esteen

    Attributes:
        image: pygame pinta joka täytetään mustaksi
        rect: pygame neliö

    """

    def __init__(self, width, height, pos_x, pos_y):
        """Luokan konstruktori
        Args:
            width: esteen leveys
            height: esteen korkeus
            pos_x: esteen x koordinaatti
            pos_y: esteen y koordinaatti

        """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos_x, pos_y
