import highscores.highscore_handler
import pygame
import sys


class EndMenu:
    def __init__(self, level, name, score, screen, bg_color) -> None:
        self.clock = pygame.time.Clock()
        self.level = level
        self.screen = screen
        self.bg_color = bg_color
        self.name = name
        self.score = score
        self.font = pygame.font.SysFont("Arial", 24)

        handler = highscores.highscore_handler.Highscores(self.level)
        handler.add_score(self.name, self.score)
        self.topscores = handler.find_top(10)
        for row in self.topscores:
            print(row["name"], row["score"])

    def start(self):
        while True:
            if self._loop():
                return True

    def _loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True

                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            self._render()
            self.clock.tick(60)
            pygame.display.flip()
            return False

    def _render(self):
        self.screen.fill(self.bg_color)
        self._render_text()
        self._render_scoreboard(self.topscores)

    def _render_scoreboard(self, topscores):
        for counter, row in enumerate(topscores):
            if row["name"] == self.name:
                if self.score == row[1]:
                    score = self.font.render(
                        f"{row['name']}: {row['score']}", True, (0, 0, 255))
                else:
                    score = self.font.render(
                        f"{row['name']}: {row['score']}", True, (255, 255, 255))
            else:
                score = self.font.render(
                    f"{row['name']}: {row['score']}", True, (0, 0, 0))
            self.screen.blit(score, (400, 200+30*counter))

    def _render_text(self):
        scoreboard_text = self.font.render(
            f"Highscores on level {self.level}", True, (0, 0, 0)
        )
        self.screen.blit(scoreboard_text, ((400, 100)))
