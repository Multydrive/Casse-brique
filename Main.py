import pygame
import os
from game import Game
from pygame.locals import *

class Second():
    pygame.init()

    def play(self):

        #Generer la fenetre
        envoie = 0
        pygame.display.set_caption("Plague-Brique")
        WINDOW_WIDTH  = 1040
        WINDOW_HEIGHT = 720
        i=0
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        #Importer l'arrière plan
        background = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/bg.jpg'))

        #Charger le jeu
        game = Game()

        #Affichage
        clock = pygame.time.Clock()
        fps= 60
        temps=0
        running = True

        #Boucle infinie
        while running:

            #Definition de la police
            font = os.path.join(os.path.dirname(__file__),"assets/DS-DIGI.TTF")

            #Configuration du chrono
            temps+=1/60
            tps=str("%02d mn %02d sec %02d" % (int(temps)//60, int(temps)%60, (temps*100)%100))
            chronos= Second().text_format(tps, font, 20, (0, 0, 0))

            #Score
            new_points = game.points
            new_points = str(new_points)
            score= Second().text_format("SCORE : "+ new_points, font, 25, (0, 0, 0))

            #Vie
            vies= Second().text_format("VIES : "+ str(game.balle_vie) , font, 25, (0, 0, 0))

            #Afficher la fenetre
            screen.blit(background, (0, 0))
            screen.blit(chronos,(900,10))
            screen.blit(score,(470,5))
            screen.blit(vies,(30,5))

            #Verification si il reste des vies
            if game.balle_vie == 0:
                turning = True
                click = False
                game.loose()

                while turning:

                    #Ecran de fin de partie
                    screen.blit(game.rectangle,game.rectangles)
                    pygame.draw.rect(screen, (0,0,0), game.button_1)
                    pygame.draw.rect(screen, (0,0,0), game.button_2)

                    #Gestion du highscore
                    Second().check_high_score(game.points)
                    high_score = Second().get_high_score()
                    high_score = str(high_score)
                    shore = Second().text_format("HIGH SCORE : "+ high_score, font, 25, (255, 255, 255))
                    screen.blit(shore, (470,200))
                    screen.blit(game.option, game.options)
                    screen.blit(game.exit, game.exits)
                    pygame.display.flip()

                    #Detection du click
                    mx, my = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            turning= False
                            pygame.quit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True

                    if click :
                        if game.button_1.collidepoint((mx, my)):
                            del game
                            game = Game()
                            temps=0
                            click=False
                            turning = False

                        elif game.button_2.collidepoint((mx, my)):
                            running= False
                            click=False
                            turning = False

            #Appliquer l'image du joueur
            for balle in game.all_balles:
                screen.blit(balle.image, balle.rect)

            #Appliquer l'image du joueur2
            screen.blit(game.protector.image, game.protector.rect)

            #Appliquer l'image des bonus
            for bonus in game.all_bonus:
                screen.blit(bonus.image, bonus.rect)

            #Appliquer l'image de la balle
            screen.blit(game.barre.image, game.barre.rect)
            for brick in game.wall1.wall:
                    screen.blit(brick.image,brick.rect)

            #Déplacer la balle
            for balle in game.all_balles:
                balle.deplacement()

            #Test si il reste des briques
            i = len(game.wall1.wall)
            if i == 0:
                envoie += 1
                del game.wall1
                game.spawn_mur()
                envoie_bis = envoie

                while envoie_bis > 0:
                    if game.balle.vit < 10 and game.barre.velocity < 15:
                        game.balle.vit +=1
                        game.barre.velocity += 1
                        envoie_bis -= 1

                    if game.wall1.randomMin < 5:
                        game.wall1.randomMin += 1

                    elif game.wall1.randomMin < 8:
                        game.wall1.randomMin += 1

                    elif game.wall1.randomMin >= 8:
                        game.wall1.randomMax = 10


            #Verifier la pression des touches pour le deplacement de la barre1
            if game.pressed.get(pygame.K_RIGHT) and game.barre.rect.x + game.barre.rect.width < screen.get_width() and not game.pressed.get(pygame.K_LEFT):
                game.barre.move_right()

            elif game.pressed.get(pygame.K_LEFT) and game.barre.rect.x > 0 and not game.pressed.get(pygame.K_RIGHT):
                game.barre.move_left()

            #Verifier la pression des touches pour le deplacement de la barre2
            if game.pressed.get(pygame.K_f) and game.protector.rect.x + game.protector.rect.width < screen.get_width()  and not game.pressed.get(pygame.K_s):
                game.protector.move_right()

            elif game.pressed.get(pygame.K_s) and game.protector.rect.x > 0  and not game.pressed.get(pygame.K_f):
                game.protector.move_left()

            #Mise à jour de l'ecran
            pygame.display.flip()
            clock.tick(fps)

            #Test la fermeture de la fenetre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                #Detecter si un joueur lache une touche du clavier
                elif event.type == pygame.KEYDOWN:
                    game.pressed[event.key] = True
                    if event.key == pygame.K_SPACE:
                        game.balle.fixe = 0

                    #Ecran de pause
                    if event.key == pygame.K_ESCAPE:
                        escape = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/escape.png'))
                        escape = pygame.transform.scale(escape, (300,50 ))
                        escapes = escape.get_rect()
                        escapes.x = 380
                        escapes.y = 340
                        pose = True

                        while pose:
                            screen.blit(escape,escapes)
                            pygame.display.flip()

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        running = False
                                        pose= False
                                        pygame.quit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        pose = False

                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False

            #Chute des bonus
            for bonus in game.all_bonus:
                bonus.fall

    #Creation d'un format general de text
    def text_format(self, message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    #Recuperation du highscore
    def get_high_score(self):
        high_score = 0

        try:
            #Recuperation du highscore dans le fichier
            high_score_file = open("high_score.txt", "r")
            high_score = int(high_score_file.read())
            high_score_file.close()

        except IOError:
            #Fichier vide
            pass

        except ValueError:
            #Nombre invalide
            pass

        return high_score

    #Sauvegarde du highscore
    def save_high_score(self, new_high_score):
        try:
            #Ecriture du highscore dans le fichier
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()

        except IOError:
            #Ecriture impossible
            pass

    #Verifie si obtention du highscore
    def check_high_score(self, points ):
        #Recuperation du highscore
        high_score = Second().get_high_score()
        current_score = 0

        try:
            #Recuperation du score actuel
            current_score = points

        except ValueError:
            #La valeur score n'a pas le bon format
            pass

        #Verifie si meilleur score
        if current_score > high_score:
            Second().save_high_score(current_score)
