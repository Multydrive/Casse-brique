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
        self.Protector = protector()
        self.balle_vie = 1
        self.all_bonus = []
        self.points = 0
        self.spawn_balle()
        self.spawn_mur()
        self.click = False
        #self.type_bonus = Bonus(self)

    def spawn_balle(self):
        if self.balle_vie > 0:
            self.balle = Balle(self)
            self.all_balles.append(self.balle)
    def spawn_mur(self):
        self.wall1 = Wall(self)
        

    def spawn_bonus(self, x, y):
        self.choix = random.randint(0,2)
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

    def loose(self):
        self.button_1 = pygame.Rect(50, 100 , 200 , 50)
        self.button_2 = pygame.Rect(50, 200 , 200 , 50)
        self.rectangle_blanc = pygame.Rect(0, 0, 500, 500)
        self.option = pygame.image.load('assets/restart.png')
        self.option = pygame.transform.scale(self.option , (200,50 ))
        self.options = self.option.get_rect()
        self.options.x = 50
        self.options.y = 100
        self.exit = pygame.image.load('assets/exit.jpg')
        self.exit = pygame.transform.scale(self.exit, (200,50))
        self.exits = self.option.get_rect()
        self.exits.x = 50
        self.exits.y = 200         