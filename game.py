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
        self.all_balles = []
        self.wall1 = Wall()
        self.Protector = protector()
        self.all_bonus = pygame.sprite.Group()
        self.type_bonus = Bonus()

    def lancer_balle(self):
        self.balle = Balle(self)
        self.all_balles.append(self.balle)

    def check_collision(self, sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)
