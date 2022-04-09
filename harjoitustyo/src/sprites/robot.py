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
        #print(self.height, self.width)
        #self.rect.x = 200
        #self.rect.y = 200
        print(self.rect)
    # def refresh(self):
    #     self.rect.x += self.dx
    #     self.rect.y += self.dy

    def set_x_speed(self, newdx):
        self.dx = newdx

    def set_y_speed(self, newdy):
        self.dy = newdy

    def increase_x_speed(self, acc):
        self.dx += acc

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
        self.refresh_position_x()
        if self.rect.x < 0 or self.rect.x > levelwidth:
            self.refresh_position_x_undo()
        #print(self.rect.x)
        self.refresh_position_y()
        
        
        # TODO: Update edges to be objects so collision can be checked instead of position
        # if self.rect.y > levelheight:
        #     #print("below")
        #     #print(self.rect.y)
        #     self.rect.y = levelheight - 2.5*self.height
        #     #print(self.rect.y)
        #     self.set_y_speed(0)
        # elif self.rect.y < 0:
        #     #print("above")print
        #     self.refresh_position_y_undo()
 
        