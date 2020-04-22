import pygame
from barre import Barre
from balle import Balle

class Game:

    def __init__(self):
        #générer le joueur
        self.barre = Barre()
        self.pressed = {}
        self.balle = Balle()
