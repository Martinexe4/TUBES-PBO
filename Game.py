from Menu_utama import Menu_utama
from Cara_Bermain import Cara_Bermain
from Level_1 import Level_1
from Level_2 import Level_2
from Level_3 import Level_3
from Ending import Ending
from Info import Info
from Game_loader import *
from Mouse import Mouse
from Keyboard import Keyboard

class Game:
    def __init__(self,framerate:int = 60) -> None:
        self.framerate = framerate
        self.clock = pygame.time.Clock()

        # list_halaman berisi halaman apa saja
        # yang terdapat dalam game
        # seperti suatu game terdiri dari halaman awal, halaman setting, dan lain-lain.
        # halaman bisa diartikan juga sebagai menu

        self.list_halaman = {"Menu_utama":Menu_utama(),
                             "Info":Info(),
                             "Cara_Bermain":Cara_Bermain(),
                             "Level_1":Level_1(),
                             "Level_2":Level_2(),
                             "Level_3":Level_3(),
                             "Ending":Ending()}
        
        self.list_halaman_key = self.list_halaman.keys()
        
        # atribut status halaman berisi mengenai keterangan game
        # seperti letak user berada dihalaman mana, max score,
        # tingkat kesulitan game, dan lain-lain
        self.status_game_sekarang = {"halaman_sekarang":"Menu_utama"}
        
    def mulai(self):
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    Mouse.set_mouse_keklik()

                if event.type == pygame.MOUSEMOTION:
                    Mouse.set_mouse_pos(event.pos)

                if event.type == pygame.KEYDOWN:
                    Keyboard.set_key_input(event.key)

            for key in self.list_halaman_key:
                if self.status_game_sekarang["halaman_sekarang"] == key:
                    self.list_halaman[key].Update(self.status_game_sekarang)
                    self.status_game_sekarang = self.list_halaman[key].kembalikan_status_game()
        
            pygame.display.update()
            self.clock.tick(self.framerate)


