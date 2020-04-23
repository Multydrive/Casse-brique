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

    def type_bonus(self):
        self.pos_y
        for x in range(0, 65):

            if self.pos_x >= 1040:
                self.pos_x = 0
                self.pos_y = self.pos_y + brick.rect.height

            choix = random.randint(0,3)

            if choix == 0:
                powerup = bonus((600, 0))
                powerup.image = pygame.image.load('assets/bleu.jpg')

            elif choix == 1:
                powerup = bonus((self.pos_x, self.pos_y))
                powerup.image = pygame.image.load('assets/vert.jpg')

            elif choix == 2:
                powerup = bonus((self.pos_x, self.pos_y))
                powerup.image = pygame.image.load('assets/rouge.jpg')

            elif choix == 3:
                powerup = bonus((self.pos_x, self.pos_y))
                powerup.image = pygame.image.load('assets/us.jpg')

            powerup = Bonus()
            all_bonus.add(powerup)
