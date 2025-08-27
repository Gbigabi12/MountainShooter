#!/usr/bin/python
# -*- coding: utf-8 -*-
from importlib.metadata import pass_none

import pygame

from code.level import Level
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Mountain Shooter")

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            # 1. Menu
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in MENU_OPTION[:3]:  # novos jogos ou load
                level = Level(self.window, "Level1", menu_return)
                level_return = level.run()

            elif menu_return == "QUIT":
                running = False

            # Limita FPS do loop principal
            clock.tick(60)

        pygame.quit()
        quit()
