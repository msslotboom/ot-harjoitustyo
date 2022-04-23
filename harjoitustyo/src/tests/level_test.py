from src.level import Level
import unittest
import pygame


class TestLevel(unittest.TestCase):
    def setUp(self) -> None:
        tempsize = (600, 480)
        color = (255, 87, 87)
        screen = pygame.display.set_mode(tempsize)
        self.clock = pygame.time.Clock()
        self.level = Level(screen, color)

    def test_move_left(self):
        robpos = self.level.physicsmodule.robot.rect.x, self.level.physicsmodule.robot.rect.y
        self.level.physicsmodule.robot_move_left()
        self.clock.tick(60)
        self.level.refresh()
        newrobpos = self.level.physicsmodule.robot.rect.x, self.level.physicsmodule.robot.rect.y
        self.assertTrue(robpos > newrobpos)

    def test_move_right(self):
        robpos = self.level.physicsmodule.robot.rect.x
        self.level.physicsmodule.robot_move_right()
        self.clock.tick(60)
        self.level.refresh()
        newrobpos = self.level.physicsmodule.robot.rect.x
        self.assertTrue(robpos < newrobpos)

    def test_jump(self):
        robpos = self.level.physicsmodule.robot.rect.y
        self.level.physicsmodule.robot_jump()
        self.clock.tick(60)
        self.level.refresh()
        newrobpos = self.level.physicsmodule.robot.rect.y
        self.assertTrue(robpos > newrobpos)
