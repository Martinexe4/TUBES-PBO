import pygame
from Game_loader import screen
from Halaman_Abstrak import *
from Halaman_Abstrak import Halaman
from Mobil import Rintangan_mobil, Mobil
from Player import Player
from random import randint

class Level_1(Halaman):
    def __init__(self) -> None:
        super().__init__()

        self.nama_halaman = "Level_1"
        self.Background("00-Grapich/01-bg-05.png")

        self.backgroundsound_1 = pygame.mixer.Sound("01-Audio/suara_burung.flac")
        self.backgroundsound_1.set_volume(0.1)

        self.backgroundsound_2 = pygame.mixer.Sound("01-Audio/suara_mobil.mpeg")
        self.backgroundsound_2.set_volume(0.1)

        self.player = Player("00-Grapich/Katak.png")

        self.timer  = True

        self.titik_final = pygame.Surface((20, 20))
        self.titik_final_rect = self.titik_final.get_rect(bottomright = (randint(20, 1280), randint(20, 360)))
        self.titik_final.fill("red")

        self.mobil_1 = Rintangan_mobil(2000)
        self.mobil_1.add(Mobil("topright", (400, 238), "kanan"))
        self.mobil_2 = Rintangan_mobil(2500)

        self.mobil_3 = Rintangan_mobil(2000)
        self.mobil_3.add(Mobil("topleft", (1100, 370), "kiri"))
        self.mobil_4 = Rintangan_mobil(2500)
        self.mobil_4.add(Mobil("topleft", (850, 435), "kiri"))


    def update(self):
        if self.suara == False:
            self.backgroundsound_1.play(-1)
            self.backgroundsound_2.play(-1)
            self.suara = True

        self.mobil_1.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 238), "kanan")
        self.mobil_2.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 300), "kanan")
        self.mobil_3.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 370), "kiri")
        self.mobil_4.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 435), "kiri")

        if self.titik_final_rect.colliderect(self.player.rect):
            self.status_game_sekarang["halaman_sekarang"] = "Level_2"
            self.player.reset_posisi()
            self.reset()

        if pygame.sprite.spritecollideany(self.player, self.mobil_1):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.player.reset_posisi()
            self.reset()

        if pygame.sprite.spritecollideany(self.player, self.mobil_2):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.reset()

        if pygame.sprite.spritecollideany(self.player, self.mobil_3):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.reset()

        if pygame.sprite.spritecollideany(self.player, self.mobil_4):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.reset()

    def input(self):
        if Keyboard.get_key_input() == pygame.K_RIGHT:
            self.player.bergerak("kanan", 40)

        if Keyboard.get_key_input() == pygame.K_LEFT:
            self.player.bergerak("kiri", 40)

        if Keyboard.get_key_input() == pygame.K_UP:
            self.player.bergerak("atas", 40)

        if Keyboard.get_key_input() == pygame.K_DOWN:
            self.player.bergerak("bawah", 40)

    def tampil(self):
        self.player.tampil()
        screen.blit(self.titik_final, self.titik_final_rect)
        
        self.mobil_1.tampil()
        self.mobil_2.tampil()
        self.mobil_3.tampil()
        self.mobil_4.tampil()

    def reset(self):
        self.player.reset_posisi()
        self.mobil_1.reset()
        self.mobil_2.reset()
        self.mobil_3.reset()
        self.mobil_4.reset()
        self.mobil_1.add(Mobil("topright", (400, 238), "kanan"))
        self.mobil_3.add(Mobil("topleft", (1100, 370), "kiri"))
        self.mobil_4.add(Mobil("topleft", (850, 435), "kiri"))
        self.backgroundsound_1.stop()
        self.backgroundsound_2.stop()
        self.suara = False
        self.titik_final_rect = self.titik_final.get_rect(bottomright = (randint(20, 1280), randint(20, 360)))