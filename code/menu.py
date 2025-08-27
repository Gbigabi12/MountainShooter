#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import os

from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW



class Menu:
    def __init__(self, window):
        self.window = window
        self.menu_option = 0

        # Carrega imagem de fundo
        base_path = os.path.dirname(__file__)
        asset_path = os.path.join(base_path, '..', 'asset', 'MenuBg.png')
        self.surf = pygame.image.load(asset_path).convert_alpha()
        self.rect = self.surf.get_rect(top= 0, left=0)

        # Música de fundo
        music_path = os.path.join(base_path, '..', 'asset', 'Menu.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # loop infinito

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            # 1. Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.menu_option = (self.menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_DOWN:
                        self.menu_option = (self.menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[self.menu_option]

            # 2. Desenha tudo
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, (WIN_WIDTH / 2, 70))
            self.menu_text(50, "Shooter", (255, 128, 0), (WIN_WIDTH / 2, 110))

            for i, opt in enumerate(MENU_OPTION):
                cor = COLOR_YELLOW if i == self.menu_option else COLOR_WHITE
                self.menu_text(20, opt, cor, (WIN_WIDTH / 2, 200 + 25 * i))

            # 3. Atualiza tela
            pygame.display.flip()

            # 4. Limita FPS
            clock.tick(60)

    def menu_text(self, text_size, text, color, center_pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=center_pos)
        self.window.blit(surf, rect)