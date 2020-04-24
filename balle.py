import pygame
import os
import random

class Balle(pygame.sprite.Sprite):

    #Constructeur de la balle
    def __init__(self, game,vit):
        self.game = game
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/virus.png'))
        self.image = pygame.transform.rotozoom(self.image, 0, 0.08)
        self.rect = self.image.get_rect()
        self.rect.x = self.game.barre.rect.x + self.rect.width/2
        self.rect.y = self.game.barre.rect.y - self.rect.height
        self.vit = vit
        self.velocityY =  - self.vit
        self.choix = random.randint(0,1)
        if self.choix == 0:
            self.velocityX =  self.vit
        elif self.choix == 1:
            self.velocityX = -self.vit
        self.origin_image = self.image
        self.angle = 0
        self.fixe = 1
        self.destruction = False

    #Deplacement de la balle
    def deplacement(self):
        if self.fixe == 0:
            brick = self.collision_mur_barre()
            self.rotate()
            self.rect.x += self.velocityX
            self.rect.y += self.velocityY
            if self.destruction:
                self.game.wall1.destruction_brique(brick)
                self.destruction = False

        elif self.fixe == 1:
            self.rect.x = self.game.barre.rect.x + self.rect.width/2
            self.rect.y = self.game.barre.rect.y - self.rect.height

    #Balle qui rote sur elle meme
    def rotate(self):
        self.angle += 2.5
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    #Collisions de la balle
    def collision_mur_barre(self):

        #Touche la gauche
        if self.rect.x < 0:
            self.velocityX = self.vit

        #Touche la droite
        elif self.rect.x > 1010:
            self.velocityX = - self.vit

        #Touche le bas
        elif self.rect.y > 670:
            self.vit_actuelle = self.vit
            self.game.all_balles.remove(self)
            self.game.balle_vie -= 1
            self.game.spawn_balle(self.vit_actuelle)
            self.fixe = 1

        #Touche la barre principale
        elif self.game.check_collision(self,self.game.barre):
            self.velocityY = - self.vit

        #Touche le haut
        elif self.rect.y < 35:
            self.velocityY = self.vit

        #Touche les murs
        for brick in self.game.wall1.wall:
            if self.game.check_collision(self, brick):
                self.destruction = True

                 #Balle venant de gauche
                if  brick.rect.x - self.rect.x - self.rect.width < 0 and brick.rect.x - self.rect.x - self.rect.width > -20 :
                    self.velocityX = - self.vit

                #Balle venant de droite
                elif self.rect.x - brick.rect.x - brick.rect.width < 0 and self.rect.x - brick.rect.x - brick.rect.width > -20:
                    self.velocityX = self.vit

                #Balle venant d'en haut
                if brick.rect.y - self.rect.y - self.rect.height < 0 and brick.rect.y - self.rect.y - self.rect.height > -20:
                    self.velocityY = - self.vit

                #Balle venant d'en bas
                elif self.rect.y - brick.rect.y - brick.rect.height < 0 and self.rect.y - brick.rect.y - brick.rect.height > -20:
                    self.velocityY = self.vit
                return brick
