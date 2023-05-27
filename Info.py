import pygame
from Game_loader import screen
from Halaman_Abstrak import Halaman
from Tombol import Tombol

class Info(Halaman):
    def __init__(self) -> None:
        super().__init__()

        self.nama_halaman = "Info"
        self.Background("00-Grapich/01-bg-06.png")

        self.tombol_kembali = Tombol("00-Grapich/00-tombol-back.png",pilihan=  "topleft", posisi = (30, 30))

        self.info = pygame.image.load("00-Grapich/02-info.png")
        self.info_rect = self.info.get_rect(center = (640, 360))

    def input(self):
        if self.tombol_kembali.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"

    def tampil(self):
        self.tombol_kembali.tampil()
        screen.blit(self.info, self.info_rect)
