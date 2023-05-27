import pygame
from Game_loader import screen

class Player(pygame.sprite.Sprite):
    def __init__(self,gambar_player:str = "", pilihan:str = "", posisi:tuple = (0, 0)) -> None:

        try :
            self.player = pygame.image.load(gambar_player).convert_alpha()
            self.player = pygame.transform.rotate(self.player, 180)
        except:
            self.player = pygame.Surface((50, 50))
            self.player.fill("green")
            self.player = pygame.transform.rotate(self.player, 180)

        self.player = pygame.transform.scale_by(self.player, 1.25)
        self.posisi_semula = "midbottom"
        self.posisi_semula_tuple = (screen.get_width() / 2, screen.get_height())
        self.rect = self.player.get_rect(midbottom = (self.posisi_semula_tuple))

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

        self.arah = "atas"
        self.arah_sebelumnya = "atas"

    def tampil(self):
        screen.blit(self.player, self.rect)

    def ubah_warna_player(self, warna:str):
        self.player.fill(warna)

    def bergerak(self, arah, jauh_pindah):
        if arah == "atas":
            self.rect.top -= jauh_pindah

            if self.rect.top <= 0:
                self.rect.top = 0

            self.arah = "atas"
        elif arah == "bawah":
            self.rect.top += jauh_pindah

            if self.rect.bottom >= screen.get_height():
                self.rect.bottom = screen.get_height()

            self.arah = "bawah"
        elif arah == "kanan":
            self.rect.left += jauh_pindah

            if self.rect.right >= screen.get_width():
                self.rect.right = screen.get_width()

            self.arah = "kanan"
        elif arah == "kiri":
            self.rect.left -= jauh_pindah

            if self.rect.left <= 0:
                self.rect.left = 0

            self.arah = "kiri"

        if self.arah == "atas":
            if self.arah_sebelumnya == "atas":
                pass
            elif self.arah_sebelumnya == "bawah":
                self.player = pygame.transform.rotate(self.player, 180)
            elif self.arah_sebelumnya == "kanan":
                self.player = pygame.transform.rotate(self.player, 90)
            elif self.arah_sebelumnya == "kiri":
                self.player = pygame.transform.rotate(self.player, -90)
        elif self.arah == "bawah":
            if self.arah_sebelumnya == "atas":
                self.player = pygame.transform.rotate(self.player, 180)
            elif self.arah_sebelumnya == "bawah":
                pass
            elif self.arah_sebelumnya == "kanan":
                self.player = pygame.transform.rotate(self.player, -90)
            elif self.arah_sebelumnya == "kiri":
                self.player = pygame.transform.rotate(self.player, 90)
        elif self.arah == "kanan":
            if self.arah_sebelumnya == "atas":
                self.player = pygame.transform.rotate(self.player, -90)
            elif self.arah_sebelumnya == "bawah":
                self.player = pygame.transform.rotate(self.player, 90)
            elif self.arah_sebelumnya == "kanan":
                pass
            elif self.arah_sebelumnya == "kiri":
                self.player = pygame.transform.rotate(self.player, 180)
        elif self.arah == "kiri":
            if self.arah_sebelumnya == "atas":
                self.player = pygame.transform.rotate(self.player, 90)
            elif self.arah_sebelumnya == "bawah":
                self.player = pygame.transform.rotate(self.player, -90)
            elif self.arah_sebelumnya == "kanan":
                self.player = pygame.transform.rotate(self.player, 180)
            elif self.arah_sebelumnya == "kiri":
                pass

        self.arah_sebelumnya = self.arah
    
    def reset_posisi(self):
        if self.arah == "atas" :
            pass
        elif self.arah == "bawah":
            self.player = pygame.transform.rotate(self.player, 180)
        
        elif self.arah == "kanan":
            self.player = pygame.transform.rotate(self.player, 90)

        elif self.arah == "kiri":
            self.player = pygame.transform.rotate(self.player, -90)

        self.arah = "atas"
        self.arah_sebelumnya = "atas"
        
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