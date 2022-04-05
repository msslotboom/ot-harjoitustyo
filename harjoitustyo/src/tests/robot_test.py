import unittest
from sprites.robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot()

    def test_move_left(self):
        initx = self.robot.rect.x
        self.robot.move_left()
        self.assertEqual(initx, self.robot.rect.x + 5)

    def test_move_right(self):
        initx = self.robot.rect.x
        self.robot.move_right()
        self.assertEqual(initx, self.robot.rect.x - 5)