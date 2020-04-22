import pygame

class Brique(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 3
        self.image = pygame.image.load('assets/bleu.jpg').convert()
        self.rect = self.image.get_rect()
        self.rect.x = 140
        self.rect.y = 150
