import pygame
import gameloop
import level


def main():
    pygame.init()
    bg_color = (255, 87, 87)
    size = (1920, 1080)
    screen = pygame.display.set_mode(size, pygame.SCALED)
    gamelevel = level.Level(screen, bg_color)
    loop = gameloop.Gameloop(gamelevel, screen, bg_color)
    if loop.start():
        win(gamelevel.points)
    else:
        return


def win(points):
    print(f"You won with {points} points")


if __name__ == "__main__":
    main()
