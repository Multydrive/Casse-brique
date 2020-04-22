import pygame
import random
class Brick(pygame.sprite.Sprite):
    def __init__(self, position: tuple):
        pygame.sprite.Sprite.__init__(self)

        self.image        = pygame.image.load('assets/bleu.jpg')
        self.rect         = self.image.get_rect()
        self.rect.topleft = position

class Wall(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

        self.pos_x = 0
        self.pos_y = 20

        for x in range(0, 65):

            if self.pos_x >= 1040:
                self.pos_x = 0
                self.pos_y = self.pos_y + brick.rect.height

            choix = random.randint(0,3)
            if choix == 0:
                brick = Brick((self.pos_x, self.pos_y))
                brick.image = pygame.image.load('assets/bleu.jpg')

            elif choix == 1:
                brick = Brick((self.pos_x, self.pos_y))
                brick.image = pygame.image.load('assets/vert.jpg')

            elif choix == 2:
                brick = Brick((self.pos_x, self.pos_y))
                brick.image = pygame.image.load('assets/rouge.jpg')

            elif choix == 3:
                brick = Brick((self.pos_x, self.pos_y))
                brick.image = pygame.image.load('assets/us.jpg')

            self.add(brick)
            self.pos_x = self.pos_x + brick.rect.width
