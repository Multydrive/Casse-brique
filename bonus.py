import pygame
import random

class Bonus (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/us.jpg')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.08)
        self.rect = self.image.get_rect()
        self.velocity = 2
        self.rect.y = 0

    def fall(self):
        self.rect.y += self.velocity

