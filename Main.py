import pygame
from game import Game

class Second():
    pygame.init()

    def play(self):
        # generer la fenetre
        pygame.display.set_caption("Casse-Brique")
        WINDOW_WIDTH  = 1040
        WINDOW_HEIGHT = 720
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        #importer l'arrière plan
        background = pygame.image.load('assets/bg.jpg')
        #charger notre jeu
        game = Game()
        running = True
        #boucle tant que cette condition est vraie
        while running:

            #Afficher la fenetre
            screen.blit(background, (0, 0))

            #Appliquer l'image de mon joueur
            for balle in game.all_balles:
                screen.blit(balle.image, balle.rect)

            #Appliquer l'image de mon joueur2
            screen.blit(game.Protector.image, game.Protector.rect)

            #Appliquer l'image des bonus
            game.all_bonus.draw(screen)

            #Appliquer l'image de la balle
            screen.blit(game.barre.image, game.barre.rect)
            for brick in game.wall1.wall:
                screen.blit(brick.image,brick.rect)

            #Déplacer la balle
            for balle in game.all_balles: 
                balle.deplacement()

            #verifier si le joueur veut aller à droite ou a gauche
            if game.pressed.get(pygame.K_RIGHT) and game.barre.rect.x < 960 and not game.pressed.get(pygame.K_LEFT):
                game.barre.move_right()
            elif game.pressed.get(pygame.K_LEFT) and game.barre.rect.x > 0 and not game.pressed.get(pygame.K_RIGHT):
                game.barre.move_left()

            #verifier si le second joueur veut aller à droite ou a gauche
            if game.pressed.get(pygame.K_f) and game.Protector.rect.x < 1000 and not game.pressed.get(pygame.K_s):
                game.Protector.move_right()
            elif game.pressed.get(pygame.K_s) and game.Protector.rect.x > 0  and not game.pressed.get(pygame.K_f):
                game.Protector.move_left()

            #mettre a jour l'écran
            pygame.display.flip()

            #si le joueur ferme cette fenetre
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print("Fermeture du jeu")
                #detecter si un joueur la che une touche du clavier
                elif event.type == pygame.KEYDOWN:
                    game.pressed[event.key] = True
                    if event.key == pygame.K_SPACE:
                        game.lancer_balle()
                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False

            #applique l'image des bonus
            game.all_bonus.draw(screen)

            for bonus in game.all_bonus:
                bonus.fall()
