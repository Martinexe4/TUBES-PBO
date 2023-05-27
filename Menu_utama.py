import pygame
from Halaman_Abstrak import Halaman
from Tombol import Tombol
from Mobil import Rintangan_mobil
from Game_loader import screen

class Menu_utama(Halaman):
    def __init__(self) -> None:
        super().__init__()
        self.nama_halaman = "Menu_utama"
        self.Background("00-Grapich/01-bg-05.png")
        self.backgroundsound = pygame.mixer.Sound("01-Audio/suara_jungle.mpeg")

        self.gambar = pygame.image.load("00-Grapich/02.png")
        self.gambar_rect = self.gambar.get_rect(center=(640, 360))

        self.tombol_mulai = Tombol("00-Grapich/00-tombol-play.png", pilihan= "center", posisi= (640, 320))

        self.tombol_info = Tombol("00-Grapich/00-tombol-info.png", pilihan= "center", posisi= (640, 400))

        self.tombol_keluar = Tombol("00-Grapich/00-tombol-exit.png", pilihan= "center", posisi= (640, 480))

        self.tombol_tanya_tanya = Tombol("00-Grapich/00-tandatanya.png", pilihan= "topright", posisi=(1250, 30))

        self.mobil_1 = Rintangan_mobil(2000)
        self.mobil_2 = Rintangan_mobil(1000)

        self.timer = True

    def update(self):
        if self.suara == False:
            self.backgroundsound.play(-1)
            self.suara = True
        
        self.mobil_1.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 250), "kanan")
        self.mobil_2.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 380), "kiri")

    def input(self):
        if self.tombol_mulai.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Level_1"
            self.backgroundsound.stop()
            self.mobil_1.reset()
            self.mobil_2.reset()
            self.suara = False

        if self.tombol_info.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Info"
            self.mobil_1.reset()
            self.mobil_2.reset()

        if self.tombol_keluar.diklik():
            self.mobil_1.reset()
            self.mobil_2.reset()
            pygame.quit()
            exit()

        if self.tombol_tanya_tanya.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Cara_Bermain"
            self.mobil_1.reset()
            self.mobil_2.reset()

    def tampil(self):
        self.mobil_1.tampil()
        self.mobil_2.tampil()
        screen.blit(self.gambar, (self.gambar_rect))
        self.tombol_mulai.tampil()
        self.tombol_info.tampil()
        self.tombol_keluar.tampil()
        self.tombol_tanya_tanya.tampil()