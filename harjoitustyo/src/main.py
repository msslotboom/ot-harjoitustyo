import pygame
import gameloop
import level
import menu
import end


def main():
    pygame.init()
    bg_color = (255, 87, 87)
    size = (1920, 1080)
    levelname = "level1"
    screen = pygame.display.set_mode(size, pygame.SCALED)
    gamemenu = menu.MainMenu(screen, bg_color)
    name = gamemenu.start()
    if name == "":
        name = "Unknown"
    start(levelname, name, screen, bg_color)


def start(levelname, name, screen, bg_color):
    gamelevel = level.Level(screen, bg_color, levelname)
    loop = gameloop.Gameloop(gamelevel, screen, bg_color)
    if loop.start():
        win(levelname, gamelevel.points, name, screen, bg_color)


def win(levelname, points, name, screen, bg_color):
    e = end.EndMenu(levelname, name, points, screen, bg_color)
    if e.start():
        start(levelname, name, screen, bg_color)


if __name__ == "__main__":
    main()
