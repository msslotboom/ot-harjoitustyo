import pygame
from sprites.robot import Robot

class Level:
    def __init__(self, screen) -> None:
        #initialise screen
        self.screen = screen
        self.screen.fill(((255,87,87)))
        self.robot = Robot()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)

    def _initialise_sprites(self):
        self.screen.fill((255,87,87))
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)