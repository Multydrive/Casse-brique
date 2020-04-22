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
            screen.blit(game.barre.image, game.barre.rect)

            #Appliquer l'image de la balle
            screen.blit(game.balle.image, game.balle.rect)
            game.wall.draw(screen)

            #Déplacer la balle
            game.balle.deplacement()

            #verifier si le jouerur veut aller à droite ou a gauche
            if game.pressed.get(pygame.K_RIGHT) and game.barre.rect.x < 960 and not game.pressed.get(pygame.K_LEFT):
                game.barre.move_right()
            elif game.pressed.get(pygame.K_LEFT) and game.barre.rect.x > 0 and not game.pressed.get(pygame.K_RIGHT):
                game.barre.move_left()

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
                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False
