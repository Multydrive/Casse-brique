import pygame
import os

class Balle(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/virus.png'))
        self.image = pygame.transform.rotozoom(self.image, 0, 0.08)
        self.rect = self.image.get_rect()
        self.rect.x = self.game.barre.rect.x + self.rect.width/2
        self.rect.y = self.game.barre.rect.y - self.rect.height
        self.vit = 4
        self.velocityX = - self.vit
        self.velocityY = - self.vit
        self.origin_image = self.image
        self.angle = 0
        self.fixe = 1


    def deplacement(self):
        if self.fixe == 0:
            self.collision_mur_barre()
            self.rotate()
            self.rect.x += self.velocityX
            self.rect.y += self.velocityY
        elif self.fixe == 1:
            self.rect.x = self.game.barre.rect.x + self.rect.width/2
            self.rect.y = self.game.barre.rect.y - self.rect.height

    def rotate(self):
        self.angle += 2.5
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def collision_mur_barre(self):
        for brick in self.game.wall1.wall:
            if self.game.check_collision(self, brick):
                 #balle vient de la gauche
                if  brick.rect.x - self.rect.x - self.rect.width < 0 and brick.rect.x - self.rect.x - self.rect.width > -20 :
                    self.velocityX = - self.vit
                #balle vient de la droite
                elif self.rect.x - brick.rect.x - brick.rect.width < 0 and self.rect.x - brick.rect.x - brick.rect.width > -20:
                    self.velocityX = self.vit
                #balle vient d'en haut
                if brick.rect.y - self.rect.y - self.rect.height < 0 and brick.rect.y - self.rect.y - self.rect.height > -20:
                    self.velocityY = - self.vit
                #balle vient d'en
                elif self.rect.y - brick.rect.y - brick.rect.height < 0 and self.rect.y - brick.rect.y - brick.rect.height > -20:
                    self.velocityY = self.vit
                self.game.wall1.destruction_brique(brick)
                


        #touche la gauche
        if self.rect.x < 0:
            self.velocityX = self.vit
        #touche la droite
        elif self.rect.x > 1010:
            self.velocityX = - self.vit
        # touche le bas
        elif self.rect.y > 670:
            self.game.all_balles.remove(self)
            self.game.balle_vie -= 1
            self.game.spawn_balle()
            self.fixe = 1
        #touche la barre principale
        elif self.game.check_collision(self,self.game.barre):
            self.velocityY = - self.vit
        #touche le haut
        elif self.rect.y < 35:
            self.velocityY = self.vit
