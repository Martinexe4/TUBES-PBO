import pygame
from Game_loader import screen

class Rintangan_mobil(pygame.sprite.Group):
    def __init__(self, periode:int) -> None:
        super().__init__()
        self.periode = periode

        self.a = 0
        self.b = 0

    def tambah_rintangan(self, lama_halaman_active, posisi_semula:str, posisi_semula_tuple:tuple, arah:str, jauh_pindah = 3):
        if lama_halaman_active // self.periode == self.a:
            self.b = 1

        if self.b == 1:
            self.add(Mobil(posisi_semula, posisi_semula_tuple, arah, jauh_pindah))
            self.a = self.a + 1
            self.b = 0

    def tampil(self):
        self.update()
        self.draw(screen)

    def reset(self):
        self.empty()
        self.a = 0
        self.b = 0

class Mobil(pygame.sprite.Sprite):
    def __init__(self,posisi_semula:str, posisi_semula_tuple:tuple, arah:str, jauh_pindah = 3) -> None:
        super().__init__()
        self.arah = arah
        self.jauh_pindah = jauh_pindah

        if self.arah == "kanan":
            pass
        elif self.arah == "kiri":
            pass
        elif self.arah == "atas":
            pass
        elif self.arah == "bawah":
            pass

        self.image = pygame.image.load("00-Grapich/ambulance.png").convert_alpha()

        if self.arah == "kiri":
            pass
        elif self.arah == "kanan":
            self.image = pygame.transform.rotate(self.image, 180)
        elif self.arah == "bawah":
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.arah == "atas":
            self.image = pygame.transform.rotate(self.image, -90)
            
        self.posisi_semula = posisi_semula
        self.posisi_semula_tuple = posisi_semula_tuple
        
        if self.posisi_semula == "topleft":
            self.rect = self.image.get_rect(topleft = posisi_semula_tuple)
        elif self.posisi_semula == "topright" :
            self.rect = self.image.get_rect(topright = posisi_semula_tuple)
        elif self.posisi_semula == "bottomright" :
            self.rect = self.image.get_rect(bottomright = posisi_semula_tuple)
        elif self.posisi_semula == "bottomleft" :
            self.rect = self.image.get_rect(bottomleft = posisi_semula_tuple)
        elif self.posisi_semula == "midbottom" :
            self.rect = self.image.get_rect(midbottom = posisi_semula_tuple)
        elif self.posisi_semula == "midtop" :
            self.rect = self.image.get_rect(midtop = posisi_semula_tuple)
        elif self.posisi_semula == "midright" :
            self.rect = self.image.get_rect(midright = posisi_semula_tuple)
        elif self.posisi_semula == "midleft" :
            self.rect = self.image.get_rect(midleft = posisi_semula_tuple)
        elif self.posisi_semula == "center" :
            self.rect = self.image.get_rect(center = posisi_semula_tuple)

    def update(self) -> None:
        if self.arah == "kanan":
            self.rect.x += self.jauh_pindah
        elif self.arah == "kiri":
            self.rect.x -= self.jauh_pindah
        elif self.arah == "atas":
            self.rect.y -= self.jauh_pindah
        elif self.arah == "bawah":
            self.rect.y += self.jauh_pindah

        if self.rect.left >= screen.get_width():
            self.kill()
        
        if self.rect.top >= screen.get_height():
            self.kill()

        if self.rect.right <= 0:
            self.kill()

        if self.rect.bottom <= 0:
            self.kill()