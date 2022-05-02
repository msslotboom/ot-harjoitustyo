import pygame


class Gameloop():
    """Peli silmukka: päivittää pelin tilaa, sisältää tapahtumankäsitteliän
    """
    def __init__(self, level, screen, bg_color) -> None:
        """Luokan konstruktori
        Args:
            level: pelin taso
            screen: peliruutu
            bg_color: ruudun taustaväri
        """
        self.clock = pygame.time.Clock()
        self.screen = screen
        pygame.display.toggle_fullscreen()
        self.bg_color = bg_color
        self.gamelevel = level
        self.physicsmodule = self.gamelevel.physicsmodule

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.physicsmodule.robot_move_left()
                if event.key == pygame.K_RIGHT:
                    self.physicsmodule.robot_move_right()
                if event.key == pygame.K_UP:
                    self.physicsmodule.robot_jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.physicsmodule.robot_stop_left()
                if event.key == pygame.K_RIGHT:
                    self.physicsmodule.robot_stop_right()
        return True

    def render(self):
        self.screen.fill(self.bg_color)
        self.gamelevel.all_sprites.draw(self.screen)
        refresh_return = self.gamelevel.refresh()
        if refresh_return is not False:
            return refresh_return
        pygame.display.flip()
        self.clock.tick(60)
        return False

    def start(self):
        while True:
            if self.handle_events() is False:
                break
            render_return = self.render()
            if render_return is not False:
                return render_return
