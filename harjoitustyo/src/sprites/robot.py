import pygame, os
dirname = os.path.dirname(__file__)

class Robot(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.width = self.rect[2]
        self.height = self.rect[3]
        self.dx = 0
        self.dy = 0
        self.jumping = False

    def set_x_speed(self, newdx):
        self.dx = newdx

    def set_y_speed(self, newdy):
        self.dy = newdy

    def increase_x_speed(self, acc):
        self.dx += acc

    def start_jump(self, jumpspeed):
        self.jumping = True
        self.set_y_speed(-jumpspeed)

    def stop_jump(self):
        self.jumping = False
        self.set_y_speed(0)

    def refresh_position_x(self):
        self.rect.x += self.dx

    def refresh_position_y(self):
        self.rect.y += self.dy

    def refresh_position_x_undo(self):
        self.rect.x += -self.dx

    def refresh_position_y_undo(self):
        self.rect.y += -self.dy

    def cancel_robot_x_movement(self):
        self.set_x_speed(0)

    def cancel_robot_y_movement(self):
        self.set_y_speed(0)

    def robot_update_pos(self, screensize):
        levelheight, levelwidth = screensize[0], screensize[1]
        # TODO: To be changed when vertical barriers are added, + this should be checked in level not in robot
        self.refresh_position_x()
        if self.rect.x < 0 or self.rect.x > levelwidth:
            self.refresh_position_x_undo()
        self.refresh_position_y()
        