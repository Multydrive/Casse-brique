import pygame
import os

class Protector(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 3
        self.max_health = 3
        self.velocity = 10
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/barre.jpg'))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 570

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
