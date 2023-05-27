import pygame
from Game_loader import screen
from Halaman_Abstrak import *
from Halaman_Abstrak import Halaman
from Player import Player
from Mobil import Rintangan_mobil, Mobil
from random import randint

class Level_2(Halaman):
    def __init__(self) -> None:
        super().__init__()

        self.nama_halaman = "Level_2"
        self.Background("00-Grapich/01-bg-06.png")

        self.player = Player("00-Grapich/Katak.png")

        self.timer = True

        self.titik_final = pygame.Surface((20, 20))
        self.titik_final_rect = self.titik_final.get_rect(bottomright = (randint(20, 1280), randint(20, 360)))
        self.titik_final.fill("red")

        self.backgroundsound_1 = pygame.mixer.Sound("01-Audio/suara_burung.flac")
        self.backgroundsound_1.set_volume(0.1)

        self.backgroundsound_2 = pygame.mixer.Sound("01-Audio/suara_mobil.mpeg")
        self.backgroundsound_2.set_volume(0.1)

        self.mobil_1 = Rintangan_mobil(1800)
        self.mobil_1.add(Mobil("topleft", (1000, 70), "kiri"))

        self.mobil_2 = Rintangan_mobil(2500)
        self.mobil_2.add(Mobil("topleft", (900, 135), "kiri"))

        self.mobil_3 = Rintangan_mobil(1600)

        self.mobil_4 = Rintangan_mobil(2500)

        self.mobil_5 = Rintangan_mobil(1900)
        self.mobil_6 = Rintangan_mobil(2500)

        self.mobil_7 = Rintangan_mobil(2600)
        self.mobil_7.add(Mobil("topright", (200, 535), "kanan"))

        self.mobil_8 = Rintangan_mobil(2500)
        self.mobil_8.add(Mobil("topright", (300, 600), "kanan"))

    def update(self):
        if self.suara == False:
            self.backgroundsound_1.play(-1)
            self.backgroundsound_2.play(-1)
            self.suara = True

        self.mobil_1.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 70), "kiri")
        self.mobil_2.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 135), "kiri")
        self.mobil_3.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 200), "kiri")
        self.mobil_4.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 265), "kiri")
        self.mobil_5.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 405), "kanan")
        self.mobil_6.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 470), "kanan")
        self.mobil_7.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 535), "kanan")
        self.mobil_8.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 600), "kanan")

        if self.titik_final_rect.colliderect(self.player.rect):
            self.status_game_sekarang["halaman_sekarang"] = "Level_3"
            self.reset()

        if pygame.sprite.spritecollideany(self.player, self.mobil_1):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
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

        if pygame.sprite.spritecollideany(self.player, self.mobil_5):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.reset()
        
        if pygame.sprite.spritecollideany(self.player, self.mobil_6):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.reset()

        if pygame.sprite.spritecollideany(self.player, self.mobil_7):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.reset()

        if pygame.sprite.spritecollideany(self.player, self.mobil_8):
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
        screen.blit(self.titik_final,self.titik_final_rect)
        self.mobil_1.tampil()
        self.mobil_2.tampil()
        self.mobil_3.tampil()
        self.mobil_4.tampil()
        self.mobil_5.tampil()
        self.mobil_6.tampil()
        self.mobil_7.tampil()
        self.mobil_8.tampil()

    def reset(self):
        self.player.reset_posisi()
        self.mobil_1.reset()
        self.mobil_2.reset()
        self.mobil_3.reset()
        self.mobil_4.reset()
        self.mobil_5.reset()
        self.mobil_6.reset()
        self.mobil_7.reset()
        self.mobil_8.reset()
        self.suara = False
        self.backgroundsound_1.stop()
        self.backgroundsound_2.stop()
        self.titik_final_rect = self.titik_final.get_rect(bottomright = (randint(20, 1280), randint(20, 360)))
        self.mobil_1.add(Mobil("topleft", (1000, 70), "kiri"))
        self.mobil_2.add(Mobil("topleft", (900, 135), "kiri"))
        self.mobil_7.add(Mobil("topright", (200, 535), "kanan"))
        self.mobil_8.add(Mobil("topright", (300, 600), "kanan"))
