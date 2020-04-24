import pygame
from pygame.locals import *
import os
from Main import Second
from game import *

class Start_Menu():
    #Initialisation
    pygame.init()

    #Centrer application
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    #Affichage
    def text_format(self,message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)

        return newText

    # Main Menu
    def main_menu(self):

        # Game Framerate
        clock = pygame.time.Clock()
        FPS=30

        font = "assets/Retro.ttf"

        #Resolution
        screen_width=1040
        screen_height=720

        screen=pygame.display.set_mode((screen_width, screen_height))
        menu=True
        selected="start"

        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        selected="start"
                    elif event.key==pygame.K_DOWN:
                        selected="quit"
                    if event.key==pygame.K_RETURN:
                        if selected=="start":
                            Second().play()
                        if selected=="quit":
                            pygame.quit()
                            quit()

            # Affichage menu
            bg = pygame.image.load('assets/wallpaper.jpg')
            screen.blit(bg, (0,0))
            title=Start_Menu().text_format("Plague-Brique", font, 90, (255, 0, 0))
            if selected=="start":
                text_start=Start_Menu().text_format("START", font, 75, (239, 216, 7))
            else:
                text_start =Start_Menu().text_format("START", font, 75, (0, 0, 0))
            if selected=="quit":
                text_quit=Start_Menu().text_format("QUIT", font, 75, (239, 216, 7))
            else:
                text_quit = Start_Menu().text_format("QUIT", font, 75, (0, 0, 0))

            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()

            # Textes menu
            screen.blit(title, (int(screen_width/2) - int((title_rect[2]/2)), 180))
            screen.blit(text_start, (int(screen_width/2) - (int(start_rect[2]/2)), 360))
            screen.blit(text_quit, (int(screen_width/2) - (int(quit_rect[2]/2)), 420))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Casse-Brique_Groupe9")


Start_Menu().main_menu()
pygame.quit()
quit()
