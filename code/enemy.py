#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import PLAYER_KEY_UP, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, WIN_HEIGHT, WIN_WIDTH, \
    PLAYER_KEY_LEFT
from code.entity  import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
