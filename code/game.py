#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT



class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Meu Jogo")

    def run(self):
        # Mostra o menu apenas uma vez no início
        menu = Menu(self.window)
        menu.run()

        # Agora vem o loop do jogo
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill((0, 0, 0))
            # desenhar jogo aqui...
            pygame.display.flip()

        pygame.quit()
