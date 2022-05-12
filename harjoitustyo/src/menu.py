import sys
import pygame


class MainMenu:
    def __init__(self, screen, bg_color) -> None:
        self.name = ""
        self.font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.width, self.height = screen.get_size()[0], screen.get_size()[1]
        self.clock = pygame.time.Clock()
        self.bg_color = bg_color
        self.screen.fill((bg_color))

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return self.name

                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                    else:
                        self.name += event.unicode
            self.render()
            self.clock.tick(60)
            pygame.display.flip()

    def render(self):
        """Rendering of robot, text etc
        """
        self.screen.fill(self.bg_color)
        self._render_exit_text()
        self._render_text_box()
        self._render_name_text()

    def _render_exit_text(self):
        esc_text = self.font.render(
            "Press esc to exit the game!", True, (0, 0, 0)
        )
        self.screen.blit(esc_text, (self.width-350, 50))

    def _render_name_text(self):
        name_text = self.font.render(
            f"{self.name}", True, (0, 0, 0)
        )
        self.screen.blit(name_text, ((self.width/2)-200, self.height/2))

    def _render_text_box(self):
        text_box = pygame.Surface([self.width/5, 30])
        text_box.fill((255, 255, 255))
        box_text = self.font.render(
            "Enter your name: ", True, (0, 0, 0)
        )
        self.screen.blit(box_text, ((self.width/2)-400, self.height/2))
        self.screen.blit(text_box, (self.width/2-200, self.height/2))
