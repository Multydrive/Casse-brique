import pygame
from brique import *

class Balle(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load('assets/virus.png')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.08)
        self.rect = self.image.get_rect()
        self.rect.x = 470
        self.rect.y = 600
        self.velocityX = -4
        self.velocityY = -4
        self.origin_image = self.image
        self.angle = 0


    def deplacement(self):
        self.collision_mur_barre()
        #self.rotate()
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

    """def rotate(self):
        self.angle += 2.5
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)"""

    def collision_mur_barre(self):
        for brick in self.game.wall1.wall:
            if self.game.check_collision(self, brick):
                 #balle vient de la gauche
                if  brick.rect.x - self.rect.x - self.rect.width < 0 and brick.rect.x - self.rect.x - self.rect.width > -20 :
                    self.velocityX = -4
                #balle vient de la droite
                elif self.rect.x - brick.rect.x - brick.rect.width < 0 and self.rect.x - brick.rect.x - brick.rect.width > -20:
                    self.velocityX = 4
                #balle vient d'en haut
                if brick.rect.y - self.rect.y - self.rect.height < 0 and brick.rect.y - self.rect.y - self.rect.height > -20:
                    self.velocityY = -4
                #balle vient d'en
                elif self.rect.y - brick.rect.y - brick.rect.height < 0 and self.rect.y - brick.rect.y - brick.rect.height > -20:
                    self.velocityY = 4
                self.game.wall1.destruction_brique(brick)
                self.game.spawn_bonus(brick.rect.x, brick.rect.y)
                

        #touche la gauche
        if self.rect.x < 0:
            self.velocityX = 4
        #touche la droite
        elif self.rect.x > 1010:
            self.velocityX = -4
        # touche le bas
        elif self.rect.y > 670:
            self.game.all_balles.remove(self)
            print("Vie restant :" +  str(self.game.balle_vie))
            self.game.balle_actuelle = 0
        #touche la barre principale
        elif self.game.check_collision(self,self.game.barre):
            self.velocityY = -4
        #touche le haut
        elif self.rect.y < 35:
            self.velocityY = 4
