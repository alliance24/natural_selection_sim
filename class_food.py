import pygame
import random
import constantes


class Food():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("assets/Rond_rouge.png"), (12, 12))
        self.rect = self.image.get_rect()
        self.eat = False
        self.max_x = int(constantes.LARGEUR_GENERAL)
        self.max_y = int(constantes.HAUTEUR_GENERAL)
        self.x = random.randint(14, self.max_x)
        self.y = random.randint(14, self.max_y) 

    def get_rect(self):
        return self.rect
              

    def Clear(self):
        surface = pygame.Surface(self.image.get_size())
        surface.fill("white")

    def Afficher(self, fenetre):
        fenetre.blit(self.image, (self.x, self.y))



    