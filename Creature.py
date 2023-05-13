
import pygame
import constantes
import random

# Création des entités

class Creature(pygame.sprite.Sprite):
    
    def __init__(self):
        # Appelle le init de la classe hérité
        super().__init__()
        self.speed = 1
        self.deplacement = 50
        self.size = 1
        self.food = 1
        self.view = 1
        self.image = pygame.transform.scale(pygame.image.load("assets/rubiks.png"), (18, 18))
        self.rect = self.image.get_rect()
        self.alive = True
        self.max_x = int(constantes.LARGEUR_GENERAL)
        self.max_y = int(constantes.HAUTEUR_GENERAL)
        self.x = random.randint(0, self.max_x)
        self.y = random.randint(0, self.max_y)
        
        
    def move(self):
        
        self.x += random.randint(-(self.speed*self.deplacement), (self.speed*self.deplacement))
        self.y += random.randint(-(self.speed*self.deplacement), (self.speed*self.deplacement))

        # Vérifier si l'image est sortie de la surface
        if self.x < 0:
            self.x = 18
        elif self.x > self.max_x:
            self.x = self.max_x
        if self.y < 0:
            self.y = 18
        elif self.y > self.max_y:
            self.y = self.max_y

    
    def Afficher(self, fenetre):
        fenetre.blit(self.image, (self.x, self.y))
        # Mettre à jour l'affichage
        pygame.display.update()

        
        
        
        


# , speed, size, food, view