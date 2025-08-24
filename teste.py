#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

pygame.init()
window = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Janela de Teste")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((30, 30, 30))  # cor de fundo cinza
    pygame.display.flip()

pygame.quit()
