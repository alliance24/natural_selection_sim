import pygame
import constantes
from Creature import *
import queue
from queue import liste
from queue import liste_food
from class_food import *

class Simulation:
    def __init__(self, nb_creature):
        self.nb_creature = nb_creature
        for individu in range(self.nb_creature):
            individu = Creature()
            queue.add(liste, individu)
        
        
    def Mise_A_Jour(self) -> None:
        #Ce qui est différent d'une frame à l'autre; toutes les actualisations se font ici
        
        for individu in liste:
            if individu.alive == True:
                individu.move()
                for food in liste_food:
                    if food.eat == False:
                        if individu.eat(food.get_rect()):
                            food.eat = True
        
            
        # for food in liste_food:
        #     if individu.eat(food.get_rect()):
        #         food.eat = True
                
        
        
        

    def Afficher(self, fenetre) -> None:
        #Une fois que tous les calculs ont été faits dans la fonction Mise_A_Jour, on affiche tous les éléments
        
        #On commence par effacer l'écran de la frame précédante en coloriant l'écran
        
                    
        fenetre.fill("white")

        
        
        self.surface_general = pygame.Surface((constantes.LARGEUR_GENERAL, constantes.HAUTEUR_GENERAL)) # dimensions (largeur-hauteur)
        self.surface_settings = pygame.Surface((constantes.LARGEUR_SETTINGS, constantes.HAUTEUR_SETTINGS))
        self.surface_stats = pygame.Surface((constantes.LARGEUR_STATS, constantes.HAUTEUR_STATS))
        
        
        
        self.surface_general.fill("black")  # couleur rouge
        self.surface_stats.fill("green")  # couleur verte
        self.surface_settings.fill("blue")  # couleur bleu
        
        fenetre.blit(self.surface_settings, (constantes.X_SETTINGS, constantes.Y_SETTINGS))
        fenetre.blit(self.surface_stats, (constantes.X_STATS, constantes.Y_STATS))
        
        for individu in liste:
            if individu.alive == True:
                individu.Afficher(self.surface_general)
                
        for food in liste_food:
            if food.eat == False:
                food.Afficher(self.surface_general)
                    
                    
                    
        # for food in liste_food:
        #         if food.eat == False:
        #             food.Afficher(self.surface_general)
        #             # food.Clear()
        
        # for individu in liste:
        #     if individu.alive == True:
        #         individu.Afficher(self.surface_general)
        #         # individu.Clear()
                
        
        
        fenetre.blit(self.surface_general, (constantes.X_GENERAL, constantes.Y_GENERAL)) # coordonnées (x, y)
        
 

        #Suite de la fonction pour afficher les textes, tout ça est séparé dans une fonction annexe pour pas polluer 
        # self.__Affichage_Ecriture(fenetre)
        
    def Nouveau_tour(self):
        
        for individu in liste:
            if not individu.alive:
                liste.retirer(individu)
        
        


    
    




