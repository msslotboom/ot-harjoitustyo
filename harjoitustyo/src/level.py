import os
import pygame
from sprites.barrier import Barrier
from sprites.robot import Robot
from sprites.goal import Goal
from physics import Physics
dirname = os.path.dirname(__file__)


class Level:
    """Luokka joka luo tason ja päivittää attribuuttien lokaatiot.

    Attributes:
        screen: pygame screen
        font: fontti jolla pistemäärä ja muu teksti kirjoitetaan
        width: pygame näyton leveys
        height: pygame näyton korkeus
        barrierwidth: esteen leveyden oletusarvo
        robot: robotti attribuutti jota pelaaja ohjaa
        goal: maali jonne robotin pitää päästä voittaakseen
        all_sprites: sprite group joka sisältää pelin kaikki spritetit
        robotgroup: sprite group joka sisältää pelin robottiatribuutin
        all_barriers: sprite group joka sisältää kaikki esteet
        points: pistemäärä
        physicsmodule: pelin fysiikkamoduuli joka on physics luokka
    """

    def __init__(self, screen, bg_color) -> None:
        """Luokan konstruktori, joka luo uuden tason

        Args:
            screen: pygame näyttö jonne taso rakennetaan
            bg_color: näytön taustaväri
        """

        # initialise screen
        self.screen = screen
        self.screen.fill((bg_color))

        self.font = pygame.font.SysFont("Arial", 24)

        self.width, self.height = screen.get_size()[0], screen.get_size()[1]
        self.barrierwidth = 20
        self.robot = Robot(0, self.height - self.barrierwidth/2)
        self.goal = Goal(20, 2.75*self.height/5)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.robot)
        self.all_sprites.add(self.goal)

        self.robotgroup = pygame.sprite.Group()
        self.robotgroup.add(self.robot)

        self.all_barriers = pygame.sprite.Group()

        self.points = 1000000

        # Add this as a parameter in init once level selector is ready
        self._read_level(dirname+"/levels/level1.csv")

        self.physicsmodule = Physics(
            self.robot, self.goal, self.all_sprites, self.all_barriers)

    def _read_level(self, filename):
        """Lataa tason esteet .csv tiedostosta

        Args:
            filename: tiedoston nimi josta ladataan esteet
        """
        with open(filename, encoding="utf-8") as file:
            for row in file:
                parts = row.split(",")
                if parts[0] == "Barrier":
                    for index, part in enumerate(parts):
                        parts[index] = parts[index].strip()
                        if "levelheight" in part:
                            parts[index] = parts[index].replace(
                                "levelheight", str(self.height))
                        if "levelwidth" in part:
                            parts[index] = parts[index].replace(
                                "levelwidth", str(self.width))
                        if "barrierwidth" in part:
                            parts[index] = parts[index].replace(
                                "barrierwidth", str(self.barrierwidth))
                        if "\n" in part:
                            parts[index] = parts[index].replace("\n", "")
                    evaluatedlist = []
                    for i in range(1, 5):
                        evaluatedlist.append(eval(parts[i]))
                    newbarrier = Barrier(
                        evaluatedlist[0], evaluatedlist[1], evaluatedlist[2], evaluatedlist[3])
                    self.all_sprites.add(newbarrier)
                    self.all_barriers.add(newbarrier)

    def refresh(self):
        """Funktio joka lataa tason muutokset. Palauttaa True jos pelaaja voitti tason
        """
        self.points -= 1
        self._render_points()
        self._render_exit_text()
        if self.physicsmodule.refresh():
            return True
        return False

    def _render_points(self):
        """Näyttää pistemäärän ruudussa
        """
        point_text = self.font.render(
            f"Points: {self.points}", True, (0, 0, 0))
        self.screen.blit(point_text, (50, 50))

    def _render_exit_text(self):
        """Näyttää tekstin joka kertoo miten peli suljetaan
        """
        esc_text = self.font.render(
            "Press esc to exit the game!", True, (0, 0, 0)
        )
        self.screen.blit(esc_text, (self.width-350, 50))
