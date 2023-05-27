import pygame
from Halaman_Abstrak import *
from Halaman_Abstrak import Halaman

class Ending(Halaman):
    def __init__(self) -> None:
        super().__init__()

        self.nama_halaman = "Cara_Bermain"
        self.Background("00-Grapich/01-bg-09.png")

        self.backgroundsound = pygame.mixer.Sound("01-Audio/lagu_bang_windah.mp3")
        self.backgroundsound.set_volume(1.5)

    def update(self):
        if self.suara == False:
            self.backgroundsound.play(-1)
            self.suara = True

    def input(self):
        if Keyboard.get_key_input() == pygame.K_SPACE:
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.backgroundsound.stop()

    def tampil(self):
        pass
