import pygame, os
dirname = os.path.dirname(__file__)

class Robot(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.rect = self.image.get_rect()
        self.width = self.rect[2]
        self.length = self.rect[3]

        self.dx = 0
        self.dy = 0

    def refresh(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def set_x_speed(self, newdx):
        self.dx = newdx

    def set_y_speed(self, newdy):
        self.dx = newdy

    def refresh_position_x(self):
        self.rect.x += self.dx

    def refresh_position_y(self):
        self.rect.y += self.dy

    def refresh_position_x_undo(self):
        self.rect.x += -self.dx

    def refresh_position_y_undo(self):
        self.rect.y += -self.dy
 
    

    # Obselete

    # def move_left(self):
    #     self.rect.x -= 5

    # def move_right(self):
    #     self.rect.x += 5
        