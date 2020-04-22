import pygame
from pygame.locals import *
import os

#Initialisation
pygame.init()

#Centrer application
os.environ['SDL_VIDEO_CENTERED'] = '1'

#Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

#Affichage
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

#Postion
font = "assets/Retro.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():

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
                        print("Start")
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Affichage menu
        bg = pygame.image.load('assets/wallpaper.jpg')
        screen.blit(bg, (0,0))
        title=text_format("Casse-Brique", font, 90, (255, 0, 0))
        if selected=="start":
            text_start=text_format("START", font, 75, (255, 255, 255))
        else:
            text_start = text_format("START", font, 75, (0, 0, 0))
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, (255, 255, 255))
        else:
            text_quit = text_format("QUIT", font, 75, (0, 0, 0))

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Text menu
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Casse-Brique_Groupe9")

#A mettre dans Main
main_menu()
pygame.quit()
quit()
