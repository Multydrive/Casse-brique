import pygame
import random
class Brick(pygame.sprite.Sprite):
    def __init__(self, position: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image        = pygame.image.load('assets/bleu.jpg')
        self.rect         = self.image.get_rect()
        self.rect.topleft = position

class Wall(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.i= 0
        pygame.sprite.Group.__init__(self)
        self.wall = []
        trou = 0
        self.pos_x = 0
        self.pos_y = 30

        for x in range(0, 65):
            if self.pos_x >= 1040:
                self.pos_x = 0
                self.pos_y = self.pos_y + brick.rect.height
            for brick in self.wall:
                self.i += 1
            if trou < 20 and self.i > 0:
                choix = random.randint(0,4)
            else :
                choix = random.randint(0,3)

            if choix == 0:
                brick = Brick((self.pos_x, self.pos_y))
                brick.image = pygame.image.load('assets/bleu.jpg')
                self.wall.append(brick)
            elif choix == 1:
                brick = Brick((self.pos_x, self.pos_y))
                brick.image = pygame.image.load('assets/vert.jpg')
                self.wall.append(brick)
            elif choix == 2:
                brick = Brick((self.pos_x, self.pos_y))
                brick.image = pygame.image.load('assets/rouge.jpg')
                self.wall.append(brick)
            elif choix == 3:
                brick = Brick((self.pos_x, self.pos_y))
                brick.image = pygame.image.load('assets/us.jpg')
                self.wall.append(brick)
            elif choix == 4:
                trou += 1
                pass


            self.pos_x = self.pos_x + brick.rect.width
    def destruction_brique(self,brick):
        self.wall.remove(brick)
        self.game.points += 10
