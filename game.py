import pygame
from barre import Barre
from balle import Balle
from brique import *
from Protector import *
from bonus import *


class Game:

    def __init__(self):
        #générer le joueur
        self.barre = Barre()
        self.pressed = {}
        self.balle = Balle(self)
        self.wall = Wall()
        self.Protector = protector()
        self.all_bonus = pygame.sprite.Group()
        self.type_bonus = Bonus()

    def check_collision(self):
        return pygame.sprite.collide_rect(self.balle, self.barre)
