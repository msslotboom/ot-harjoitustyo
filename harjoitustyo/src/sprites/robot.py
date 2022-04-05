import pygame, os
dirname = os.path.dirname(__file__)

class Robot(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.rect = self.image.get_rect()
        # self.x = self.rect.x
        # self.y = self.rect.y
        self.width = self.rect[2]
        self.length = self.rect[3]

    def move_left(self):
        self.rect.x -= 5

    def move_right(self):
        self.rect.x += 5
        