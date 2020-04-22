import pygame

class Balle:
    def __init__(self):
        self.image = pygame.image.load('assets/virus.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.08)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 450
        self.velocity = 2

    def deplacement(self):
        self.rect.x -= self.velocity
        self.rect.y += self.velocity