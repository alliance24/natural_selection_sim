import random
import pygame

class Food():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficher(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, 100, 100))


    