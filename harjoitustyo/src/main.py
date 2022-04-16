import pygame
import gameloop


def main():
    pygame.init()
    bg_color = (255, 87, 87)
    size = (600, 480)
    loop = gameloop.Gameloop(bg_color, size)
    if loop.start():
        win()
    else:
        return

def win():
    print("You won!")

if __name__ == "__main__":
    main()
