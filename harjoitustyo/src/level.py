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
        self.goal = Goal(20, 2.75*self.height/5)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)
        self.all_sprites.add(self.goal)

        self.robotgroup = pygame.sprite.Group()
        self.robotgroup.add(self.robot)

        self.all_barriers = pygame.sprite.Group()

        # Add this as a parameter in init once level selector is ready
        self.read_level(dirname+"/levels/level1.csv")

        self.physicsmodule = Physics(
            self.robot, self.goal, self.all_sprites, self.all_barriers)

    def read_level(self, filename):
        with open(filename, encoding="utf-8") as file:
            for row in file:
                parts = row.split(",")
                if parts[0] == "Barrier":
                    for index, part in enumerate(parts):
                        parts[index] = parts[index].strip()
                        if "levelheight" in part:
                            parts[index] = parts[index].replace(
                                "levelheight", str(self.height))
                        if "levelwidth" in part:
                            parts[index] = parts[index].replace(
                                "levelwidth", str(self.width))
                        if "barrierwidth" in part:
                            parts[index] = parts[index].replace(
                                "barrierwidth", str(self.barrierwidth))
                        if "\n" in part:
                            parts[index] = parts[index].replace("\n", "")
                    evaluatedlist = []
                    for i in range(1, 5):
                        evaluatedlist.append(eval(parts[i]))
                    newbarrier = Barrier(
                        evaluatedlist[0], evaluatedlist[1], evaluatedlist[2], evaluatedlist[3])
                    self.all_sprites.add(newbarrier)
                    self.all_barriers.add(newbarrier)

    def _initialise_sprites(self):
        self.screen.fill((255, 87, 87))

    def refresh(self):
        if self.physicsmodule.refresh():
            return True
        return False
