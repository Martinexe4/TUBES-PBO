import pygame
from Game_loader import screen
from Mouse import Mouse

# Class tombol dapat digunakan untuk membuat tombol.
# Kita bisa memilih gambar tertentu yang dapat kita jadikan icon/background dari tombol.

# Jika kita memilih memilih gambar untuk dijadikan icon/background dari tombol,
# maka secara default tombol akan berbentuk persegi panjang berwarna abu-abu.

class Tombol:
    def __init__(self, file_icon_tombol:str = "",  pilihan:str = "", posisi:tuple = (0,0)) -> None:
        self.file_icon_tombol = file_icon_tombol
        self.sorot_1 = False
        self.sorot_2 = True

        try :
            self.icon = pygame.image.load(file_icon_tombol).convert_alpha()
            self.file_icon_tombol = file_icon_tombol
        except:
            self.icon = pygame.Surface((100, 50))
            self.icon.fill("gray")
            self.icon_warna_default = "gray"

        self.suara_keklik = pygame.mixer.Sound("01-Audio/suara_keklik.ogg")
        self.posisi_semula = "midbottom"
        self.posisi_semula_tuple = (screen.get_width() / 2, screen.get_height() / 2)
        self.rect = self.icon.get_rect(midbottom = (self.posisi_semula_tuple))

        if pilihan == "topleft":
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.topleft = posisi
        elif pilihan == "topright" :
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.topright = posisi
        elif pilihan == "bottomright" :
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.bottomright = posisi
        elif pilihan == "bottomleft" :
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.bottomleft = posisi
        elif pilihan == "midbottom" :
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.midbottom = posisi
        elif pilihan == "midtop" :
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.midtop = posisi
        elif pilihan == "midright" :
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.midright = posisi
        elif pilihan == "midleft" :
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.midleft = posisi
        elif pilihan == "center" :
            self.posisi_semula = pilihan
            self.posisi_semula_tuple = posisi
            self.rect.center = posisi

    def ubah_warna_tombol(self, warna):
        self.icon.fill(warna)
    
    def tampil(self):
        if  self.rect.collidepoint(Mouse.mouse_pos_x(),Mouse.mouse_pos_y()) and self.sorot_2 == True:
            self.sorot_1 = True
            self.icon.fill((30, 30, 30), special_flags= pygame.BLEND_RGB_SUB)
            self.sorot_2 = False

        if self.rect.collidepoint(Mouse.mouse_pos_x(),Mouse.mouse_pos_y()) == False and self.sorot_2 == False:
            self.sorot_1 = False
            try :
                self.icon = pygame.image.load(self.file_icon_tombol)
            except:
                self.icon.fill(self.icon_warna_default)
            
            self.sorot_2 = True

        screen.blit(self.icon, self.rect)

    def diklik(self):
        if self.rect.collidepoint(Mouse.mouse_pos_x(),Mouse.mouse_pos_y()) and Mouse.get_mouse_keklik():
            self.suara_keklik.play()
            return True
        else:
            return False
        
    # method ubah_posisi_tombol berfungsi untuk mengubah posisi dari tombol
    def ubah_posisi_tombol(self, pilihan:str, posisi:tuple):
        if pilihan == "topleft":
            self.rect.topleft = posisi
        elif pilihan == "topright" :
            self.rect.topright = posisi
        elif pilihan == "bottomright" :
            self.rect.bottomright = posisi
        elif pilihan == "bottomleft" :
            self.rect.bottomleft = posisi
        elif pilihan == "midbottom" :
            self.rect.midbottom = posisi
        elif pilihan == "midtop" :
            self.rect.midtop = posisi
        elif pilihan == "midright" :
            self.rect.midright = posisi
        elif pilihan == "midleft" :
            self.rect.midleft = posisi
        elif pilihan == "center" :
            self.rect.center = posisi

    def Icon(self, file_icon_tombol:str):
        try :
            self.icon = pygame.image.load(file_icon_tombol).convert_alpha()
            self.file_icon_tombol = file_icon_tombol
            self.rect = self.icon.get_rect(midbottom = (self.posisi_semula_tuple))

            if self.posisi_semula == "topleft":
                self.rect.topleft = self.posisi_semula_tuple
            elif self.posisi_semula == "topright" :
                self.rect.topright = self.posisi_semula_tuple
            elif self.posisi_semula == "bottomright" :
                self.rect.bottomright = self.posisi_semula_tuple
            elif self.posisi_semula == "bottomleft" :
                self.rect.bottomleft = self.posisi_semula_tuple
            elif self.posisi_semula == "midbottom" :
                self.rect.midbottom = self.posisi_semula_tuple
            elif self.posisi_semula == "midtop" :
                self.rect.midtop = self.posisi_semula_tuple
            elif self.posisi_semula == "midright" :
                self.rect.midright = self.posisi_semula_tuple
            elif self.posisi_semula == "midleft" :
                self.rect.midleft = self.posisi_semula_tuple
            elif self.posisi_semula == "center" :
                self.rect.center = self.posisi_semula_tuple
        except:
            pass


    
    

    

        


    