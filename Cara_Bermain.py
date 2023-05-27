import pygame
from Game_loader import screen
from Halaman_Abstrak import Halaman
from Tombol import Tombol

class Cara_Bermain(Halaman):
    def __init__(self) -> None:
        super().__init__()

        self.nama_halaman = "Cara_Bermain"
        self.Background("00-Grapich/01-bg-06.png")

        self.tombol_kembali = Tombol("00-Grapich/00-tombol-back.png",pilihan=  "topleft", posisi = (30, 30))

        self.cara_bermain = pygame.image.load("00-Grapich/02-cara.png")
        self.cara_bermain_rect = self.cara_bermain.get_rect(center = (640, 360))

    def input(self):
        if self.tombol_kembali.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"

    def tampil(self):
        self.tombol_kembali.tampil()
        screen.blit(self.cara_bermain, self.cara_bermain_rect)
