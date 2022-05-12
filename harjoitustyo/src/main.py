import pygame
import gameloop
import level
import menu


def main():
    pygame.init()
    bg_color = (255, 87, 87)
    size = (1920, 1080)
    screen = pygame.display.set_mode(size, pygame.SCALED)
    gamelevel = level.Level(screen, bg_color)
    loop = gameloop.Gameloop(gamelevel, screen, bg_color)
    gamemenu = menu.MainMenu(screen, bg_color)
    name = gamemenu.start()
    if loop.start():
        win(gamelevel.points, name)
    else:
        return


def win(points, name):
    print(f"You won with {points} points, {name}")


if __name__ == "__main__":
    main()
