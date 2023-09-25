import pygame
from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game

        self.x = TILESIZE * x
        self.y = TILESIZE * y
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

