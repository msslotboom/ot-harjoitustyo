import pygame
import level

def main():
    pygame.init()
    info = pygame.display.Info()
    size = (info.current_w, info.current_h)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    gamelevel = level.Level(screen)

    running = True
    while running:
        screen.fill((255,87,87))
        gamelevel.all_sprites.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gamelevel.robot.move_left()
                if event.key == pygame.K_RIGHT:
                    gamelevel.robot.move_right()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()