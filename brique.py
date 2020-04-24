import pygame
import random
import os
class Brick(pygame.sprite.Sprite):
    def __init__(self, position: tuple,pv,type):
        pygame.sprite.Sprite.__init__(self)
        self.image        = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/bleu.jpg'))
        self.rect         = self.image.get_rect()
        self.rect.topleft = position
        self.pv_brique = pv
        self.type =type
       

class Wall(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.i= 0
        self.run = 0
        pygame.sprite.Group.__init__(self)
        self.wall = []
        trou = 0
        self.pos_x = 0
        self.pos_y = 30
        vide = 11
        self.randomMin = 0
        self.randomMax = 11

        for x in range(0, 5):
            if self.pos_x >= 1040:
                self.pos_x = 0
                self.pos_y = self.pos_y + brick.rect.height
            for brick in self.wall:
                self.i += 1
            if trou < 20 and self.i > 0:
                choix = random.randint(self.randomMin,self.randomMax)
            else :
                choix = random.randint(self.randomMin,self.randomMax - 1)

            if choix < 5:
                brick = Brick((self.pos_x, self.pos_y),1,1)
                brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/bleu.jpg'))
                self.wall.append(brick)
            elif choix >= 5 and choix <= 7:
                brick = Brick((self.pos_x, self.pos_y),2,2)
                brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/vert.jpg'))
                self.wall.append(brick)
                self.pv_brique = 2
            elif choix == 8 or choix == 9:
                brick = Brick((self.pos_x, self.pos_y),3,3)
                brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/rouge.jpg'))
                self.wall.append(brick)
                self.pv_brique=2
            elif choix == 10:
                brick = Brick((self.pos_x, self.pos_y),4,4)
                brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/us.jpg'))
                self.wall.append(brick)
                self.pv_brique = 2
            elif choix == vide:
                trou += 1
                pass


            self.pos_x = self.pos_x + brick.rect.width
    def destruction_brique(self,brick):
        brick.pv_brique -= 1
        if brick.pv_brique == 0:
            if brick.type== 1:
               self.game.points += 10 
            elif brick.type  ==  2 : 
                self.game.points += 20
            elif brick.type == 3 :
                self.game.points += 35
            elif brick.type == 4:
                self.game.points += 50 
            self.game.spawn_bonus(brick.rect.x, brick.rect.y)
            self.wall.remove(brick)
            
        elif brick.pv_brique >0:
                if brick.type  ==  2 :  
                    if brick.pv_brique == 1:
                        brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/vert.fissuré1.png'))
                elif brick.type == 3 :
                    if brick.pv_brique == 2:
                        brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/rouge.fissuré1.png'))
                    elif brick.pv_brique == 1:
                        brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/rouge.fissuré2.png'))
                elif brick.type == 4:
                    if brick.pv_brique == 3:
                        brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/us.fissuré1.png'))
                    elif brick.pv_brique == 2:
                        brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/us.fissuré2.png'))
                    elif brick.pv_brique == 1:
                        brick.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/us.fissuré3.png'))