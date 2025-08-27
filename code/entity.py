from abc import abstractmethod, ABC

import pygame
import os

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name

        # Corrige o caminho para a imagem
        base_path = os.path.dirname(os.path.dirname(__file__))  # Sobe dois níveis
        image_path = os.path.join(base_path, "asset", name + ".png")

        self.surf = pygame.image.load(image_path).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0


    @abstractmethod
    def move(self, ):
        pass
