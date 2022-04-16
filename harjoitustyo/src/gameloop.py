import pygame
import level


class Gameloop():
    def __init__(self, bg_color, size) -> None:
        self.clock = pygame.time.Clock()
        self.tempsize = (size)
        self.screen = pygame.display.set_mode(self.tempsize)
        self.gamelevel = level.Level(self.screen)
        self.bg_color = bg_color

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.gamelevel.robot_move_left()
                if event.key == pygame.K_RIGHT:
                    self.gamelevel.robot_move_right()
                if event.key == pygame.K_UP:
                    self.gamelevel.robot_jump()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.gamelevel.robot_move_right()
                if event.key == pygame.K_RIGHT:
                    self.gamelevel.robot_move_left()
            return True

    def render(self):
        self.screen.fill(self.bg_color)
        self.gamelevel.all_sprites.draw(self.screen)
        self.gamelevel.refresh()
        pygame.display.flip()
        self.clock.tick(60)

    def start(self):
        while True:
            if self.handle_events() is False:
                break
            self.render()
