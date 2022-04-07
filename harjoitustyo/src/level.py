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

        self.robotspeed = 5
        

    def _initialise_sprites(self):
        self.screen.fill((255,87,87))
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)

    def robot_move_left(self):
        self.robot.set_x_speed(-(self.robotspeed))

    def robot_move_right(self):
        self.robot.set_x_speed((self.robotspeed))

    def cancel_x_movement(self):
        self.robot.set_x_speed(0)


    
    # Checks wether position is outside of x coordinates, sides of screen need to be made objects once objects are added
    def robot_update_pos(self):
        width, height = self.screen.get_size()

        self.robot.refresh_position_x()
        if self.robot.rect.x < 0 or self.robot.rect.y > width:
            self.robot.refresh_position_x_undo()
        

        if self.robot.rect.y < 0 or self.robot.rect.y > height:
            self.robot.refresh_position_y_undo()
            