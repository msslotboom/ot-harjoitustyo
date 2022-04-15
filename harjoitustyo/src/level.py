import pygame
from sprites.barrier import Barrier
from sprites.robot import Robot
from sprites.goal import Goal


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

        self.goal = Goal(self.width-70, self.height-25)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)
        self.all_sprites.add(self.floor)
        self.all_sprites.add(self.roof)
        self.all_sprites.add(self.left_barrier)
        self.all_sprites.add(self.right_barrier)
        self.all_sprites.add(self.goal)

        self.robotgroup = pygame.sprite.Group()
        self.robotgroup.add(self.robot)

        self.barriergroup = pygame.sprite.Group()
        self.barriergroup.add(self.floor)
        self.barriergroup.add(self.roof)
        self.barriergroup.add(self.left_barrier)
        self.barriergroup.add(self.right_barrier)

        self.gravity = 1
        self.robotweight = 0.3
        self.robotspeed = 5

    def _initialise_sprites(self):
        self.screen.fill((255, 87, 87))

    def robot_move_left(self):
        self.robot.increase_x_speed(-(self.robotspeed))

    def robot_move_right(self):
        self.robot.increase_x_speed((self.robotspeed))

    def robot_jump(self):
        self.robot.start_jump(7)

    def robot_left_right_collision(self, c_b):
        if self.robot.rect.right in range(c_b.rect.left, c_b.rect.right):
            self.robot.rect.right = c_b.rect.left
        elif self.robot.rect.left in range(c_b.rect.left, c_b.rect.right):
            self.robot.rect.left = c_b.rect.right

    def robot_barrier_collision(self, collisions):
        # change this to be compatible with multiplayer
        for collision in collisions:
            c_b = collisions[collision][0] #collsion_barrier
            b_in_robot = c_b.rect.bottom in range(
                self.robot.rect.top, self.robot.rect.bottom)
            t_in_robot = c_b.rect.top in range(
                self.robot.rect.top, self.robot.rect.bottom)
            if (c_b.rect.bottom > self.robot.rect.bottom and c_b.rect.top < self.robot.rect.top):
                self.robot_left_right_collision(c_b)

            # check if top is above or bottom is below but not both -> possible top/bottom collision
            elif (b_in_robot) ^ (t_in_robot):
                r_in_b = self.robot.rect.right in range(
                    c_b.rect.left, c_b.rect.right)
                l_in_b = self.robot.rect.left in range(
                    c_b.rect.left, c_b.rect.right)
                if (r_in_b) ^ (l_in_b):
                    self.robot_left_right_collision(c_b)

                elif c_b.rect.bottom in range(self.robot.rect.top, self.robot.rect.bottom):
                    self.robot.rect.top = c_b.rect.bottom
                    self.robot.cancel_robot_y_movement()
                elif c_b.rect.top in range(self.robot.rect.top, self.robot.rect.bottom):
                    self.robot.stop_jump()
                    self.robot.rect.bottom = c_b.rect.top

    def refresh(self):
        collisions = pygame.sprite.groupcollide(
            self.robotgroup, self.barriergroup, False, False)

        self.robot_barrier_collision(collisions)

        self.robot.robot_update_pos()
        if self.robot.jumping:
            self.robot.set_y_speed(
                self.robot.dy + self.robotweight * self.gravity)
