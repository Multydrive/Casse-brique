import pygame
from game import Game
from pygame.locals import *

class Second():
    pygame.init()
    def play(self):
        # generer la fenetre
        pause = True
        envoie = 0
        pygame.display.set_caption("Casse-Brique")
        WINDOW_WIDTH  = 1040
        WINDOW_HEIGHT = 720
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        #importer l'arrière plan
        background = pygame.image.load('assets/bg.jpg')
        #charger notre jeu
        game = Game()

        #Affichage

        clock = pygame.time.Clock()
        fps= 60
        temps=0
        running = True
        #boucle tant que cette condition est vraie
        while running:
            while pause == False:
                envoie = 1000
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                            pause = True

            temps+=1/60
            tps=str("%02d mn %02d sec %02d" % (int(temps)//60, int(temps)%60, (temps*100)%100))
            font = "assets/DS-DIGI.TTF"
            chronos= Second().text_format(tps, font, 20, (0, 0, 0))

            Second().end_menu(game.points, tps, font, screen)
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
                        game.lancer_balle()
                    if event.key == pygame.K_ESCAPE:
                        pygame.time.wait(envoie)
                        pause = False
                        print("test")
                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False

            for bonus in game.all_bonus:
                bonus.fall()

    def text_format(self, message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    def end_menu(self, point, tps, font, screen):
        score_go= Second().text_format("SCORE : "+ str(point), font, 50, (0, 0, 0))
        chronos_go= Second().text_format("TEMPS : " + str(tps), font, 50, (0, 0, 0))
        again_go= Second().text_format("Pour continuer appuyer sur espace", font, 50, (0 ,0 ,0))
        bg_go = pygame.image.load('assets/wallpaper.jpg')

        score_go_rect=score_go.get_rect()
        chronos_go_rect=chronos_go.get_rect()
        again_go_rect=again_go.get_rect()

        screen.blit(bg_go,(0,0))
        screen.blit(score_go,(int(1040/2) - int((score_go_rect[2]/2)),260))
        screen.blit(chronos_go,(int(1040/2) - int((chronos_go_rect[2]/2)),360))
        screen.blit(again_go,(int(1040/2) - int((again_go_rect[2]/2)),460))
