import pygame
from player import *
from settings import *
from screens import *
import tkinter
from tkinter import ttk
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = ""
    def groups(self):
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.tiles = pygame.sprite.Group()
        self.tiles.add()
























