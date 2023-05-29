import pygame, random, constantes

class Food():
    
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("assets/Rond_rouge.png"), (constantes.TAILLE_FOOD, constantes.TAILLE_FOOD))
        self.rect = self.image.get_rect()
        self.eat = False # Etat "être mangé"
        self.max_x = int(constantes.LARGEUR_GENERAL) - constantes.TAILLE_FOOD
        self.max_y = int(constantes.HAUTEUR_GENERAL) - constantes.TAILLE_FOOD
        self.x = random.randint(14, self.max_x)
        self.y = random.randint(14, self.max_y) 

    def get_x(self):
        return self.x + constantes.TAILLE_FOOD
    
    def get_y(self):
        return self.y + constantes.TAILLE_FOOD
    
    def Clear(self):
        surface = pygame.Surface(self.image.get_size())
        surface.fill("white")

    def Afficher(self, fenetre):
        fenetre.blit(self.image, (self.x, self.y))



    