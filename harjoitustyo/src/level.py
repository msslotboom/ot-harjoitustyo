import pygame
from sprites.barrier_horizontal import Barrier_horizontal
from sprites.robot import Robot

class Level:
    def __init__(self, screen) -> None:
        
        #initialise screen
        self.screen = screen
        self.screen.fill(((255,87,87)))
        self.width, self.height = screen.get_size()[0], screen.get_size()[1]
        self.barrierwidth = 20
        self.robot = Robot(0, self.height - self.barrierwidth/2)
        self.floor = Barrier_horizontal(self.width, self.barrierwidth, self.width/2, self.height-self.barrierwidth/2)
        self.roof = Barrier_horizontal(self.width, self.barrierwidth, self.width/2, self.barrierwidth/2)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)
        self.all_sprites.add(self.floor)
        self.all_sprites.add(self.roof)

        self.robotgroup = pygame.sprite.Group()
        self.robotgroup.add(self.robot)

        self.barriergroup = pygame.sprite.Group()
        self.barriergroup.add(self.floor)
        self.barriergroup.add(self.roof)

        self.gravity = 1
        self.robotweight = 0.1
        self.robotspeed = 5
        

    def _initialise_sprites(self):
        self.screen.fill((255,87,87))

    def robot_move_left(self):
        self.robot.increase_x_speed(-(self.robotspeed))

    def robot_move_right(self):
        self.robot.increase_x_speed((self.robotspeed))


    def robot_jump(self):
        self.robot.set_y_speed(-4)

    def refresh(self):
        collisions = pygame.sprite.groupcollide(self.robotgroup, self.barriergroup, False, False)

        # TODO: change this to be compatible with multiplayer
        for collision in collisions:
            if type(collisions[collision][0]) == Barrier_horizontal:
                print(True)
                self.robot.cancel_robot_y_movement()

                # Checks wheter robot is above or below barrier and moves robot out of barrier
                distance_above_barrier = self.robot.rect.bottom - collisions[collision][0].rect.top
                distance_below_barrier = self.robot.rect.top- collisions[collision][0].rect.bottom
                if distance_above_barrier < distance_below_barrier:
                    self.robot.rect.top = collisions[collision][0].rect.bottom
                else: 
                    self.robot.rect.bottom = collisions[collision][0].rect.top

        self.robot.robot_update_pos(self.screen.get_size())
        #print(self.floor.rect)
        # Change y speed to simulate gravity TODO: change if statement, this wont work if speed mid jump is 0
        # Robot needs a "jumping" boolean that gets set to false when colliding with horizontal object and true when jump is started
        if self.robot.dy != 0:
            self.robot.set_y_speed(self.robot.dy + self.robotweight * self.gravity)
    
    # Checks wether position is outside of x coordinates, sides of screen need to be made objects once objects are added
    
   # def collision_check(self):

            