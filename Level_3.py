import pygame
from Game_loader import screen
from Halaman_Abstrak import *
from Halaman_Abstrak import Halaman
from Kereta import Rintangan_kereta, Kereta
from Mobil import Rintangan_mobil, Mobil
from Player import Player
from random import randint

class Level_3(Halaman):
    def __init__(self) -> None:
        super().__init__()

        self.nama_halaman = "Level_3"
        self.Background("00-Grapich/01-bg-07.png")

        self.player = Player("00-Grapich/Katak.png")
        self.timer = True

        self.titik_final = pygame.Surface((20, 20))
        self.titik_final_rect = self.titik_final.get_rect(bottomright = (randint(20, 1280), randint(20, 360)))
        self.titik_final.fill("red")

        self.backgroundsound_1 = pygame.mixer.Sound("01-Audio/suara_burung.flac")
        self.backgroundsound_1.set_volume(0.1)

        self.backgroundsound_2 = pygame.mixer.Sound("01-Audio/suara_mobil.mpeg")
        self.backgroundsound_2.set_volume(0.1)

        self.backgroundsound_3 = pygame.mixer.Sound("01-Audio/suara_kereta.mp3")
        self.backgroundsound_3.set_volume(0.1)

        self.kereta_1 = Rintangan_kereta(3500)
        self.kereta_2 = Rintangan_kereta(3500)

        self.mobil_1 = Rintangan_mobil(2000)
        self.mobil_1.add(Mobil("topleft", (1000, 70), "kiri", 10))

        self.mobil_2 = Rintangan_mobil(2000)
        self.mobil_2.add(Mobil("topleft", (900, 135), "kiri", 5))

        self.mobil_3 = Rintangan_mobil(2000)
        self.mobil_4 = Rintangan_mobil(2000)

        self.mobil_5 = Rintangan_mobil(2000)
        self.mobil_5.add(Mobil("topright", (200, 540), "kanan", 4))

        self.mobil_6 = Rintangan_mobil(2000)
        self.mobil_6.add(Mobil("topright", (300, 605), "kanan", 3))

    def update(self):
        if self.suara == False:
            self.backgroundsound_1.play(-1)
            self.backgroundsound_2.play(-1)
            self.backgroundsound_3.play(-1)
            self.suara = True

        self.kereta_1.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 285), "kanan")
        self.kereta_2.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 380), "kiri")

        self.mobil_1.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 70), "kiri", 10)
        self.mobil_2.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 135), "kiri", 5)
        self.mobil_3.tambah_rintangan(self.lama_halaman_aktive, "topleft", (1280, 200), "kiri", 2)

        self.mobil_4.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 475), "kanan")
        self.mobil_5.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 540), "kanan", 4)
        self.mobil_6.tambah_rintangan(self.lama_halaman_aktive, "topright", (0, 605), "kanan", 3)

        if self.titik_final_rect.colliderect(self.player.rect):
            self.status_game_sekarang["halaman_sekarang"] = "Ending"
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

        if pygame.sprite.spritecollideany(self.player, self.kereta_1):
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"
            self.reset()

        if pygame.sprite.spritecollideany(self.player, self.kereta_2):
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
        self.kereta_1.tampil()
        self.kereta_2.tampil()
        self.mobil_1.tampil()
        self.mobil_2.tampil()
        self.mobil_3.tampil()
        self.mobil_4.tampil()
        self.mobil_5.tampil()
        self.mobil_6.tampil()

    def reset(self):
        self.player.reset_posisi()
        self.kereta_1.reset()
        self.kereta_2.reset()
        self.mobil_1.reset()
        self.mobil_2.reset()
        self.mobil_3.reset()
        self.mobil_4.reset()
        self.mobil_5.reset()
        self.mobil_6.reset()
        self.suara = False
        self.backgroundsound_1.stop()
        self.backgroundsound_2.stop()
        self.backgroundsound_3.stop()
        self.titik_final_rect = self.titik_final.get_rect(bottomright = (randint(20, 1280), randint(20, 360)))
        self.mobil_1.add(Mobil("topleft", (1000, 70), "kiri", 10))
        self.mobil_2.add(Mobil("topleft", (900, 135), "kiri", 5))
        self.mobil_5.add(Mobil("topright", (200, 540), "kanan", 4))
        self.mobil_6.add(Mobil("topright", (300, 605), "kanan", 3))
