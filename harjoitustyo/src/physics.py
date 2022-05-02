import pygame


class Physics:
    def __init__(self, robot, goal, all_sprites, all_barriers) -> None:
        self.robot = robot
        self.robotgroup = pygame.sprite.Group()
        self.robotgroup.add(self.robot)
        self.goal = goal
        self.all_sprites = all_sprites
        self.all_barriers = all_barriers
        # self.gravity = 1
        self.robotweight = 0.3
        # self.robotspeed = 5
        self.robot.set_x_speed(-(5))
        self.barrier_under_robot = None
        self.previous_should_fall = None

    def _robot_left_right_collision(self, c_b):
        if self.robot.rect.right in range(c_b.rect.left, c_b.rect.right):
            self.robot.rect.right = c_b.rect.left
        elif self.robot.rect.left in range(c_b.rect.left, c_b.rect.right):
            self.robot.rect.left = c_b.rect.right

    def _robot_top_bottom_collision(self, c_b):
        if c_b.rect.bottom in range(self.robot.rect.top, self.robot.rect.bottom):
            self.robot.rect.top = c_b.rect.bottom
            self.robot.cancel_robot_y_movement()
        elif c_b.rect.top in range(self.robot.rect.top, self.robot.rect.bottom):
            self.barrier_under_robot = c_b
            self.robot.stop_jump()
            self.robot.rect.bottom = c_b.rect.top

    def _robot_barrier_collision(self, collisions):
        for collision in (collisions):
            c_b = collisions[collision][0]  # c_b = collsion_barrier
            b_in_robot = c_b.rect.bottom in range(
                self.robot.rect.top, self.robot.rect.bottom)
            t_in_robot = c_b.rect.top in range(
                self.robot.rect.top, self.robot.rect.bottom)
            if (c_b.rect.bottom > self.robot.rect.bottom and c_b.rect.top < self.robot.rect.top):
                self._robot_left_right_collision(c_b)

            # check if top is above or bottom is below but not both -> possible top/bottom collision
            elif (b_in_robot) ^ (t_in_robot):
                r_in_b = self.robot.rect.right in range(
                    c_b.rect.left, c_b.rect.right)
                l_in_b = self.robot.rect.left in range(
                    c_b.rect.left, c_b.rect.right)
                if (r_in_b) ^ (l_in_b):
        # change this to be compatible with multiplayer
                    self._robot_left_right_collision(c_b)
                else:
                    self._robot_top_bottom_collision(c_b)

    def _robot_goal_collision(self):
        goal_b_left = self.goal.rect.bottomleft
        goal_x_range = range(
            goal_b_left[0]-20, goal_b_left[0] + self.goal.width+20)
        goal_y_range = range(
            goal_b_left[1] - self.goal.height, goal_b_left[1]+10)
        if self.robot.rect.bottomleft[0] in (goal_x_range):
            if self.robot.rect.bottomleft[1] in (goal_y_range):
                return True
        return False

    def _should_robot_fall(self):
        c_b = self.barrier_under_robot
        if c_b == "":
            return True
        # if c_b.rect.top in range(self.robot.rect.bottom-1, self.robot.rect.bottom+1):
        if c_b.rect.top == self.robot.rect.bottom:
            if c_b.rect.left in range(self.robot.rect.left, self.robot.rect.right):
                return False
            if c_b.rect.right in range(self.robot.rect.left, self.robot.rect.right):
                return False
        return True

    def refresh(self):
        """Päivittää kaikkien 
        """
        collisions = pygame.sprite.groupcollide(
            self.robotgroup, self.all_barriers, False, False)
        self._robot_barrier_collision(collisions)
        if self._robot_goal_collision():
            return True

        self.robot.robot_update_pos()
        should_robot_fall = self._should_robot_fall()
        if self.previous_should_fall != should_robot_fall:
            if should_robot_fall is True and self.robot.jumping == 0:
                self.robot.start_jump(1)
        self.previous_should_fall = should_robot_fall

        if self.robot.jumping:
            self.robot.set_y_speed(
                self.robot.d_y + 0.3)
        return False

    def robot_move_left(self):
        self.robot.move_left()

    def robot_stop_left(self):
        self.robot.stop_left()

    def robot_move_right(self):
        self.robot.move_right()

    def robot_stop_right(self):
        self.robot.stop_right()

    def robot_jump(self):
        self.robot.start_jump(7)
