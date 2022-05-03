import os
import pygame
dirname = os.path.dirname(__file__)


class Robot(pygame.sprite.Sprite):
    """Luokka tekee robotin
    Attributes:
        image: pygame kuva johon ladataan robotin kuva
        rect: pygame neliö
        width: neliön leveys
        height: neliön korkeus
        d_x: robotin x nopeus
        d_y: robotin y nopeus
        left: liikkuuko robotti vasemalle
        right: liikkuuko robotti oikealle
        jumping: hyppiikö robotti, 0 = ei hypi, 1 = yksi hyppy tehty, 2 = molemmat hypyt käytetty
    """

    def __init__(self, pos_x=0, pos_y=0):
        """Luokan konstruktori
        Args:
            pos_x: robotin x koordinaatti
            pos_y: robotin y koordinaatti
        """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "robot.png")
        )

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (pos_x, pos_y)
        self.width = self.rect[2]
        self.height = self.rect[3]
        self.d_x = 0
        self.d_y = 0
        self.left = False
        self.right = False
        self.jumping = 0

    def set_x_speed(self, newdx):
        """Muuttaa robotin x nopeuden
        Args:
            newdx: uusi nopeus
        """
        self.d_x = newdx

    def set_y_speed(self, newdy):
        """Muuttaa robotin y nopeuden
        Args:
            newdy: uusi nopeus
        """
        self.d_y = newdy

    def increase_x_speed(self, acc):
        """Lisää robotin x nopeutta
        Args:
           acc: nopeus joka lisätään robotin x nopeuteen
        """
        self.d_x += acc

    def move_left(self):
        """Muuttaa vasen attribuutin todeksi
        """
        self.left = True

    def stop_left(self):
        """Muuttaa vasen attribuutin epätodeksi
        """
        self.left = False

    def move_right(self):
        """Muuttaa oikea attribuutin todeksi
        """
        self.right = True

    def stop_right(self):
        """Muuttaa oikea attribuutin epätodeksi
        """
        self.right = False

    def start_jump(self, jumpspeed):
        """Aloittaa robotin hypyn
        Args:
            jumpspeed: asettaa robotin hypyn nopeuden
        """
        if self.jumping < 2:
            self.jumping += 1
            self.set_y_speed(-jumpspeed)

    def stop_jump(self):
        """Lopettaa robotin hypyn
        """
        self.jumping = 0
        self.set_y_speed(0)

    def refresh_position_x(self):
        """Lataa robotin x aseman uudestaan
        """
        if self.left and self.right:
            return
        if self.right:
            self.rect.x -= self.d_x
        if self.left:
            self.rect.x += self.d_x

    def refresh_position_y(self):
        """Lataa robotin y aseman uudestaan
        """
        self.rect.y += self.d_y

    def refresh_position_x_undo(self):
        """kumoaa x aseman uudestaanlataamisen
        """
        if self.left and self.right:
            return
        if self.right:
            self.rect.x += self.d_x
        if self.left:
            self.rect.x -= self.d_x

    def refresh_position_y_undo(self):
        """kumoaa y aseman uudestaanlataamisen
        """
        self.rect.y += -self.d_y

    def cancel_robot_x_movement(self):
        """Asettaa robotin x nopeuden nollaan
        """
        self.set_x_speed(0)

    def cancel_robot_y_movement(self):
        """Asettaa robotin y nopeuden nollaan
        """
        self.set_y_speed(0)

    def robot_update_pos(self):
        """Lataa robotin x ja y aseman uudestaan
        """
        self.refresh_position_x()
        self.refresh_position_y()
