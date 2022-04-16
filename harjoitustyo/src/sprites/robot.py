import os
import pygame
dirname = os.path.dirname(__file__)


class Robot(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (pos_x, pos_y)
        self.width = self.rect[2]
        self.height = self.rect[3]
        self.d_x = 0
        self.d_y = 0
        self.dir = ""
        self.jumping = False

    def set_x_speed(self, newdx):
        self.d_x = newdx

    def set_y_speed(self, newdy):
        self.d_y = newdy

    def increase_x_speed(self, acc):
        self.d_x += acc

    def start_jump(self, jumpspeed):
        self.jumping = True
        self.set_y_speed(-jumpspeed)

    def stop_jump(self):
        self.jumping = False
        self.set_y_speed(0)

    def refresh_position_x(self):
        self.rect.x += self.d_x

    def refresh_position_y(self):
        self.rect.y += self.d_y

    def refresh_position_x_undo(self):
        self.rect.x += -self.d_x

    def refresh_position_y_undo(self):
        self.rect.y += -self.d_y

    def cancel_robot_x_movement(self):
        self.set_x_speed(0)

    def cancel_robot_y_movement(self):
        self.set_y_speed(0)

    def robot_update_pos(self):
        self.refresh_position_x()
        self.refresh_position_y()
