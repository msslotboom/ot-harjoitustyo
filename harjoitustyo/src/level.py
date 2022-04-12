import pygame
from sprites.barrier import Barrier
from sprites.robot import Robot


class Level:
    def __init__(self, screen) -> None:

        # initialise screen
        self.screen = screen
        self.screen.fill(((255, 87, 87)))
        self.width, self.height = screen.get_size()[0], screen.get_size()[1]
        self.barrierwidth = 20
        self.robot = Robot(0, self.height - self.barrierwidth/2)
        self.floor = Barrier(self.width, self.barrierwidth,
                             self.width/2, self.height-self.barrierwidth/2)
        self.roof = Barrier(self.width, self.barrierwidth,
                            self.width/2, self.barrierwidth/2)
        self.left_barrier = Barrier(self.barrierwidth, self.height,
                            self.barrierwidth/2, self.height/2)
        self.right_barrier = Barrier(self.barrierwidth, self.height,
                            self.width - self.barrierwidth/2, self.height/2)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)
        self.all_sprites.add(self.floor)
        self.all_sprites.add(self.roof)
        self.all_sprites.add(self.left_barrier)
        self.all_sprites.add(self.right_barrier)

        self.robotgroup = pygame.sprite.Group()
        self.robotgroup.add(self.robot)

        self.barriergroup = pygame.sprite.Group()
        self.barriergroup.add(self.floor)
        self.barriergroup.add(self.roof)
        self.barriergroup.add(self.left_barrier)
        self.barriergroup.add(self.right_barrier)

        self.gravity = 1
        self.robotweight = 0.1
        self.robotspeed = 5

    def _initialise_sprites(self):
        self.screen.fill((255, 87, 87))

    def robot_move_left(self):
        self.robot.increase_x_speed(-(self.robotspeed))

    def robot_move_right(self):
        self.robot.increase_x_speed((self.robotspeed))

    def robot_jump(self):
        self.robot.start_jump(4)

    def refresh(self):
        collisions = pygame.sprite.groupcollide(
            self.robotgroup, self.barriergroup, False, False)

        # change this to be compatible with multiplayer
        for collision in collisions:
            collided_barrier = collisions[collision][0]
            # if collisions[collision][0].horizontal:
                # Checks wheter robot is above or below barrier and moves robot out of barrier
                # distance_above_barrier = abs(
                #     self.robot.rect.bottom - collisions[collision][0].rect.top)
                # distance_below_barrier = abs(
                    # self.robot.rect.top - collisions[collision][0].rect.bottom)

            # robot is smaller than barrier and in between edges of it -> only left/right collision possible
            if (collided_barrier.rect.bottom > self.robot.rect.bottom and collided_barrier.rect.top < self.robot.rect.top):
                if self.robot.rect.right in range(collided_barrier.rect.left, collided_barrier.rect.right):
                    self.robot.rect.right = collided_barrier.rect.left
                elif self.robot.rect.left in range(collided_barrier.rect.left, collided_barrier.rect.right):
                    self.robot.rect.left = collided_barrier.rect.right

            # check if top is above or bottom is below but not both -> possible top/bottom collision
            elif (collided_barrier.rect.bottom in range(self.robot.rect.top, self.robot.rect.bottom)) ^ (collided_barrier.rect.top in range(self.robot.rect.top, self.robot.rect.bottom)):
                if (self.robot.rect.right in range(collided_barrier.rect.left, collided_barrier.rect.right)) ^ (self.robot.rect.left in range(collided_barrier.rect.left, collided_barrier.rect.right)):
                    if self.robot.rect.right in range(collided_barrier.rect.left, collided_barrier.rect.right):                        
                        self.robot.rect.right = collided_barrier.rect.left
                    elif self.robot.rect.left in range(collided_barrier.rect.left, collided_barrier.rect.right):
                        self.robot.rect.left = collided_barrier.rect.right

                elif collided_barrier.rect.bottom in range(self.robot.rect.top, self.robot.rect.bottom):
                    self.robot.rect.top = collided_barrier.rect.bottom
                    self.robot.cancel_robot_y_movement()
                elif collided_barrier.rect.top in range(self.robot.rect.top, self.robot.rect.bottom):
                    self.robot.stop_jump()
                    self.robot.rect.bottom = collided_barrier.rect.top

            # if True ^ False:
            #     print("wee")
                # if distance_above_barrier > distance_below_barrier:
                #     self.robot.set_y_speed(0)
                #     self.robot.rect.top = collisions[collision][0].rect.bottom
                # else:
                #     self.robot.stop_jump()
                #     self.robot.rect.bottom = collisions[collision][0].rect.top

        self.robot.robot_update_pos()
        if self.robot.jumping:
            self.robot.set_y_speed(
                self.robot.dy + self.robotweight * self.gravity)
