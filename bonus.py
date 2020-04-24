import pygame
import random

class Bonus (pygame.sprite.Sprite):

    #Constructeur bonus
    def __init__(self, game, x , y, image):
        super().__init__()
        self.game = game
        self.image = image
        self.image = pygame.transform.scale(self.image, (85,65))
        self.rect = self.image.get_rect()
        self.velocity = 5
        self.rect.x = x - 18
        self.x = x
        self.rect.y = y
        self.rect.y = 200
        self.different = 2

    #Chute des bonus et verification du type de bonus
    def fall(self):
        self.rect.y += self.velocity
        if self.game.check_collision(self, self.game.protector):
            if self.different == 1:
                self.bonus_ligne()

            elif self.different == 0:
                self.bonus_vie()
            self.game.all_bonus.remove(self)

        elif self.game.check_collision(self, self.game.barre):
            if self.different == 2:
                self.malus_vie()
            self.game.all_bonus.remove(self)

    #Bonus degat colonne
    def bonus_ligne(self):
        for brick in self.game.wall1.wall:
            if brick.rect.x == self.x:
                self.game.wall1.destruction_brique(brick)

    #Bonus de point de vie
    def bonus_vie(self):
        if self.game.balle_vie < 99:
            self.game.balle_vie += 1

        else:
            self.game.balle_vie = 99

    #Malus de point de vie
    def malus_vie(self):
        if self.game.balle_vie <= 0:
            self.game.balle_vie =0
            
        else:
            self.game.balle_vie -= 1
