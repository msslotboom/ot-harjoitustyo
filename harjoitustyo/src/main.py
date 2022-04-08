import pygame
import level

def main():
    pygame.init()
    info = pygame.display.Info()
    size = (info.current_w, info.current_h)
    #temporary size, will need to be updated to be fullscreen
    tempsize = (600, 480)
    screen = pygame.display.set_mode(tempsize)
    clock = pygame.time.Clock()
    gamelevel = level.Level(screen)

    running = True

    # TODO: Gameloop to be refractored into other file
    while running:
        screen.fill((255,87,87))
        gamelevel.all_sprites.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gamelevel.robot_move_left()
                if event.key == pygame.K_RIGHT:
                    gamelevel.robot_move_right()
                if event.key == pygame.K_UP:
                    gamelevel.robot_jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    gamelevel.robot.cancel_robot_x_movement()

        gamelevel.refresh()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()