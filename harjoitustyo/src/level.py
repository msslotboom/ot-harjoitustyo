import os
import pygame
from sprites.barrier import Barrier
from sprites.robot import Robot
from sprites.goal import Goal
from physics import Physics
dirname = os.path.dirname(__file__)


class Level:
    def __init__(self, screen, bg_color) -> None:

        # initialise screen
        self.screen = screen
        self.screen.fill((bg_color))
        self.width, self.height = screen.get_size()[0], screen.get_size()[1]
        self.barrierwidth = 20
        self.robot = Robot(0, self.height - self.barrierwidth/2)
        self.goal = Goal(self.width-70, self.height-25)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)
        self.all_sprites.add(self.goal)

        self.robotgroup = pygame.sprite.Group()
        self.robotgroup.add(self.robot)

        self.all_barriers = pygame.sprite.Group()

        self.read_level(dirname+"/levels/level1.csv")

        self.physicsmodule = Physics(
            self.robot, self.goal, self.all_sprites, self.all_barriers)

    def read_level(self, filename):
        with open(filename) as file:
            for row in file:
                row.replace("\n", "")
                parts = row.split(",")
                if parts[0] == "Barrier":
                    for index, part in enumerate(parts):
                        if "levelheight" in part:
                            parts[index] = parts[index].replace(
                                "levelheight", str(self.height))
                        if "levelwidth" in part:
                            parts[index] = parts[index].replace(
                                "levelwidth", str(self.width))
                        if "barrierwidth" in part:
                            parts[index] = parts[index].replace(
                                "barrierwidth", str(self.barrierwidth))
                    newbarrier = Barrier(eval(parts[1]), eval(
                        parts[2]), eval(parts[3]), eval(parts[4]))
                    self.all_sprites.add(newbarrier)
                    self.all_barriers.add(newbarrier)

    def _initialise_sprites(self):
        self.screen.fill((255, 87, 87))

    def robot_move_left(self):
        self.robot.left = True

    def robot_stop_left(self):
        self.robot.left = False

    def robot_move_right(self):
        self.robot.right = True

    def robot_stop_right(self):
        self.robot.right = False

    def robot_jump(self):
        self.robot.start_jump(7)

    def refresh(self):
        if self.physicsmodule.refresh():
            return True