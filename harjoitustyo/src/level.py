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

        self.gravity = 1
        self.robotweight = 0.1
        self.robotspeed = 5
        

    def _initialise_sprites(self):
        self.screen.fill((255,87,87))
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)

    def robot_move_left(self):
        self.robot.set_x_speed(-(self.robotspeed))

    def robot_move_right(self):
        self.robot.set_x_speed((self.robotspeed))


    def robot_jump(self):
        self.robot.set_y_speed(-4)

    def cancel_robot_x_movement(self):
        self.robot.set_x_speed(0)

    def cancel_robot_y_movement(self):
        self.robot.set_y_speed(0)

    def refresh(self):
        self.robot.robot_update_pos(self.screen.get_size())
        
        # Change y speed to simulate gravity
        if self.robot.dy != 0:
            self.robot.set_y_speed(self.robot.dy + self.robotweight * self.gravity)
    
    # Checks wether position is outside of x coordinates, sides of screen need to be made objects once objects are added
    
            
            