
import pygame
import constantes
import random

# Création des entités

class Creature(pygame.sprite.Sprite):
    
    def __init__(self):
        # Appelle le init de la classe hérité
        super().__init__()
        
        self.speed = 1
        self.deplacement = 25 # Constante qui équivaut au nombre de pixels moyen parcouru à chaque déplacement
        self.size = 1
        self.food = 1
        self.view = 1
        
        self.image = pygame.transform.scale(pygame.image.load("assets/rubiks.png"), (18, 18))
        self.rect = self.image.get_rect()
        self.alive = True
        
        self.max_x = int(constantes.LARGEUR_GENERAL - 18)
        self.max_y = int(constantes.HAUTEUR_GENERAL - 18)
        self.x = random.randint(18, self.max_x)
        self.y = random.randint(18, self.max_y)
        
        
        
    def move(self):
        direction = random.choice(["gauche", "droite", "haut", "bas"])
        if direction == "gauche":
            self.x -= self.deplacement
        elif direction == "droite":
            self.x += self.deplacement
        elif direction == "haut":
            self.y -= self.deplacement
        else:
            self.y += self.deplacement

    # Vérifier les limites de l'écran et corriger la position si nécessaire
        if self.x < 18:
            self.x = 18
        elif self.x > self.max_x:
            self.x = self.max_x - 18
        if self.y < 18:
            self.y = 18
        elif self.y > self.max_y:
            self.y = self.max_y - 18
        
        
    
    def Afficher(self, fenetre):
        fenetre.blit(self.image, (self.x, self.y))
        # Mettre à jour l'affichage
        pygame.display.update()

        
        
        
