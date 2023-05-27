from abc import ABC, abstractclassmethod
import pygame
from Game_loader import screen
from Mouse import Mouse
from Keyboard import Keyboard

# class Halaman digunakan untuk membentuk sebuah halaman.

# Sama seperti pada class tombol, kita bisa memilih gambar 
# tertentu yang dapat kita jadikan background dari halaman.

# Jika kita memilih memilih gambar untuk dijadikan background dari halaman,
# maka secara default halaman akan berwarna hitam.

class Halaman(ABC):
    def __init__(self, file_gambar_background = "") -> None:
        self.nama_halaman = ""
        self.status_game_sekarang = dict()
        self.file_gambar_background = file_gambar_background

        try :
            self.background = pygame.image.load(file_gambar_background).convert_alpha()
        except:
            self.background= pygame.Surface((screen.get_width(), screen.get_height()))
            self.background.fill("black")
            
        self.background_rect = self.background.get_rect(topleft = (0,0))
        self.timer = False
        self.suara = False

        self.halaman_aktive = False
        self.lama_halaman_aktive = 0
        self.waktu_halaman_aktive = 0

    def Update(self,status_game_sekarang):
        self.status_game_sekarang = status_game_sekarang 

        if self.status_game_sekarang["halaman_sekarang"] == self.nama_halaman and self.halaman_aktive == False:
            self.halaman_aktive = True
            self.waktu_halaman_aktive = pygame.time.get_ticks()

        if self.timer:
            self.lama_halaman_aktive = pygame.time.get_ticks() - self.waktu_halaman_aktive

        screen.blit(self.background, (0,0))
        self.update()
        self.tampil()
        self.input()

        if self.status_game_sekarang["halaman_sekarang"] != self.nama_halaman:
            self.halaman_aktive = False
            self.lama_halaman_aktive = 0 
            self.waktu_halaman_aktive  = 0

        Mouse.reset_mouse_keklik()
        Keyboard.reset_Keyboard_input()

    def update(self):
        pass
    
    @abstractclassmethod
    def input(self):
        pass

    @abstractclassmethod
    def tampil(self):
        pass

    def reset(self):
        pass

    # method ini berfungsi untuk mengembalikan status game
    def kembalikan_status_game(self):
        return self.status_game_sekarang
    
    # method ini berfungsi untuk mengubah warna backgroung halaman
    def ubah_warna_background(self, warna):
        self.background.fill(warna)
    
    # method ini berfungsi untuk mengganti background
    def Background(self, file_gambar_background:str):
        try :
            self.background = pygame.image.load(file_gambar_background).convert_alpha()
            self.file_gambar_background = file_gambar_background
        except:
            pass
