#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import os
import time

from pygame import Surface, Rect
from pygame.font import Font
from pygame.ftfont import SysFont

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        base_path = os.path.dirname(__file__)  # pasta atual (code/)
        asset_path = os.path.join(base_path, '..', 'asset', 'MenuBg.png')
        self.surf = pygame.image.load(asset_path)
        self.rect = self.surf.get_rect(left=0, top=0)
        print("Desenhando menu...")
        self.window.blit(self.surf, self.rect)
        pygame.display.flip()
        time.sleep(3)
        print("Saindo do menu")

        music_path = os.path.join(base_path, '..', 'asset', 'Menu.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # loop infinito

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size= 50, text= "Mountain", text_color= COLOR_ORANGE, text_center_pos= (WIN_WIDTH / 2, 70))
            self.menu_text(text_size=50, text="Shooter", text_color=(255, 128, 0), text_center_pos=(WIN_WIDTH / 2, 110))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

    def run(self):


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter para começar
                        running = False

        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name= "Lucida Sans Typerwriter", size=text_size)
        text_surf: Surface= text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)