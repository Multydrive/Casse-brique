import pygame
import random
from barre import Barre
from balle import Balle
from brique import Brick, Wall
from Protector import protector
from bonus import Bonus


class Game:

    def __init__(self):
        #générer le joueur
        self.barre = Barre()
        self.pressed = {}
        self.all_balles = []
        self.wall1 = Wall(self)
        self.Protector = protector()
        self.balle_vie = 3
        self.all_bonus = []
        self.points = 0
        self.spawn_balle()
        #self.type_bonus = Bonus(self)

    def spawn_balle(self):
        if self.balle_vie > 0:
            self.balle = Balle(self)
            self.all_balles.append(self.balle)

    def spawn_bonus(self, x, y):
        self.choix = random.randint(0,8)
        if self.choix == 0:
            self.image = pygame.image.load('assets/BonusLigne.png')
            self.bonus = Bonus(self, x, y,self.image)
            self.all_bonus.append(self.bonus)
            self.bonus.different = 1
        elif self.choix == 1:
            self.image = pygame.image.load('assets/bonus.png')
            self.bonus = Bonus(self, x, y,self.image)
            self.all_bonus.append(self.bonus)
            self.bonus.different = 0
        elif self.choix == 2:
            self.image = pygame.image.load('assets/malus.png')
            self.bonus = Bonus(self, x, y,self.image)
            self.all_bonus.append(self.bonus)
            self.bonus.different = 2

    def check_collision(self, sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)
