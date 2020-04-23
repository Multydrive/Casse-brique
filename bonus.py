import pygame
import random

class Bonus (pygame.sprite.Sprite):
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

    def fall(self):
        self.rect.y += self.velocity
        if self.game.check_collision(self, self.game.Protector):
            if self.different == 1:
                self.bonus_ligne()
            elif self.different == 0:
                self.bonus_vie()
            self.game.all_bonus.remove(self)
        elif self.game.check_collision(self, self.game.barre):
            if self.different == 2:
                self.malus_vie()
            self.game.all_bonus.remove(self)

    def bonus_ligne(self):
        for brick in self.game.wall1.wall:
            if brick.rect.x == self.x:
                self.game.wall1.destruction_brique(brick)

    def bonus_vie(self):
        if self.game.balle_vie < 99:
            self.game.balle_vie += 1
        else:
            print("Trop de vie")
            self.game.balle_vie = 99
    
    def malus_vie(self):
        if self.game.balle_vie <= 0:
            self.game.balle_vie =0
        else:
            self.game.balle_vie -= 1 

