import pygame
import os

class Barre(pygame.sprite.Sprite):

    #Constructeur de la barre
    def __init__(self):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/barre.jpg'))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 700

    #Deplacement a droite
    def move_right(self):
        self.rect.x += self.velocity

    #Deplacement a gauche
    def move_left(self):
        self.rect.x -= self.velocity
