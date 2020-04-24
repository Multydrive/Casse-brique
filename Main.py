import pygame
import os
from game import Game
from pygame.locals import *

class Second():
    pygame.init()
    def play(self):
        # generer la fenetre
        envoie = 0
        pygame.display.set_caption("Casse-Brique")
        WINDOW_WIDTH  = 1040
        WINDOW_HEIGHT = 720
        i=0
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        #importer l'arrière plan
        background = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/bg.jpg'))
        #charger notre jeu
        game = Game()

        #Affichage
        clock = pygame.time.Clock()
        fps= 60
        temps=0
        running = True
        #boucle tant que cette condition est vraie

        while running:
            """while pause == False:
                envoie = 1000
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                            pause = True"""

            temps+=1/60
            tps=str("%02d mn %02d sec %02d" % (int(temps)//60, int(temps)%60, (temps*100)%100))
            font = os.path.join(os.path.dirname(__file__),"assets/DS-DIGI.TTF")
            chronos= Second().text_format(tps, font, 20, (0, 0, 0))

            #Second().end_menu(game.points, tps, font, screen)
            #score
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


            if game.balle_vie == 0:
                turning = True
                click = False
                game.loose()
                while turning:
                    screen.blit(game.rectangle,game.rectangles)
                    pygame.draw.rect(screen, (0,0,0), game.button_1)
                    pygame.draw.rect(screen, (0,0,0), game.button_2)
                    Second().check_high_score(game.points)
                    high_score = Second().get_high_score()
                    high_score = str(high_score)
                    shore = Second().text_format("HIGH SCORE : "+ high_score, font, 25, (255, 255, 255))
                    screen.blit(shore, (470,200))
                    screen.blit(game.option, game.options)
                    screen.blit(game.exit, game.exits)
                    pygame.display.flip()
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

            #Appliquer l'image de mon joueur
            for balle in game.all_balles:
                screen.blit(balle.image, balle.rect)

            #Appliquer l'image de mon joueur2
            screen.blit(game.Protector.image, game.Protector.rect)

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
            #Mur vide
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


            #verifier si le joueur veut aller à droite ou a gauche
            if game.pressed.get(pygame.K_RIGHT) and game.barre.rect.x + game.barre.rect.width < screen.get_width() and not game.pressed.get(pygame.K_LEFT):
                game.barre.move_right()
            elif game.pressed.get(pygame.K_LEFT) and game.barre.rect.x > 0 and not game.pressed.get(pygame.K_RIGHT):
                game.barre.move_left()

            #verifier si le second joueur veut aller à droite ou a gauche
            if game.pressed.get(pygame.K_f) and game.Protector.rect.x + game.Protector.rect.width < screen.get_width()  and not game.pressed.get(pygame.K_s):
                game.Protector.move_right()
            elif game.pressed.get(pygame.K_s) and game.Protector.rect.x > 0  and not game.pressed.get(pygame.K_f):
                game.Protector.move_left()

            #mettre a jour l'écran
            pygame.display.flip()
            clock.tick(fps)

            #si le joueur ferme cette fenetre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                #detecter si un joueur la che une touche du clavier
                elif event.type == pygame.KEYDOWN:
                    game.pressed[event.key] = True
                    if event.key == pygame.K_SPACE:
                        game.balle.fixe = 0
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

            for bonus in game.all_bonus:
                bonus.fall()

    def text_format(self, message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    def get_high_score(self):
        # Default high score
        high_score = 0

        try:
            high_score_file = open("high_score.txt", "r")
            high_score = int(high_score_file.read())
            high_score_file.close()
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")

        return high_score


    def save_high_score(self, new_high_score):
        try:
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()
        except IOError:
            # Hm, can't write it.
            print("Unable to save the high score.")

    def check_high_score(self, points ):
        # Get the high score
        high_score = Second().get_high_score()

        # Get the score from the current game
        current_score = 0
        try:
            # Ask the user for his/her score
            current_score = points
        except ValueError:
            # Error, can't turn what they typed into a number
            print("I don't understand what you typed.")
        # See if we have a new high score
        if current_score > high_score:
            print("Yea! New high score!")
            Second().save_high_score(current_score)
        else:
            print("Better luck next time.")


    """def end_menu(self, point, tps, font, screen):
        score_go= Second().text_format("SCORE : "+ str(point), font, 50, (0, 0, 0))
        chronos_go= Second().text_format("TEMPS : " + str(tps), font, 50, (0, 0, 0))
        again_go= Second().text_format("Pour continuer appuyer sur espace", font, 50, (0 ,0 ,0))
        bg_go = pygame.image.load(os.path.join(os.path.dirname(__file__),'assets/wallpaper.jpg'))

        score_go_rect=score_go.get_rect()
        chronos_go_rect=chronos_go.get_rect()
        again_go_rect=again_go.get_rect()

        screen.blit(bg_go,(0,0))
        screen.blit(score_go,(int(1040/2) - int((score_go_rect[2]/2)),260))
        screen.blit(chronos_go,(int(1040/2) - int((chronos_go_rect[2]/2)),360))
        screen.blit(again_go,(int(1040/2) - int((again_go_rect[2]/2)),460))"""
