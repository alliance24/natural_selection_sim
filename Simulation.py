import pygame
import constantes
from Creature import *
from queue import liste

class Simulation:
    def __init__(self, nb_creature):
        self.nb_creature = nb_creature
        for individu in range(self.nb_creature):
            individu = Creature()
            liste.append(individu)
        
    def Mise_A_Jour(self) -> None:
        #Ce qui est différent d'une frame à l'autre; toutes les actualisations se font ici

        #On itère dans la file d'individus pour appeler leur propre fonction Mise_A_Jour
        #Pour itérer à travers une file, on Defile chaque élément (chaque individu) un à un, on lance sa fonction Mise_A_Jour puis on le fait revenir à la fin de la file
        for individu in liste:
            individu.move()

    def Afficher(self, fenetre) -> None:
        #Une fois que tous les calculs ont été faits dans la fonction Mise_A_Jour, on affiche tous les éléments du jeu
        
        #On commence par effacer l'écran de la frame précédante en coloriant l'écran de blanc
        fenetre.fill((255,255,255))

        self.surface_general = pygame.Surface((constantes.LARGEUR_GENERAL, constantes.HAUTEUR_GENERAL)) # dimensions (largeur-hauteur)
        self.surface_settings = pygame.Surface((constantes.LARGEUR_SETTINGS, constantes.HAUTEUR_SETTINGS))
        self.surface_stats = pygame.Surface((constantes.LARGEUR_STATS, constantes.HAUTEUR_STATS))
        
        fenetre.blit(self.surface_general, (constantes.X_GENERAL, constantes.Y_GENERAL)) # coordonnées (x, y)
        fenetre.blit(self.surface_settings, (constantes.X_SETTINGS, constantes.Y_SETTINGS))
        fenetre.blit(self.surface_stats, (constantes.X_STATS, constantes.Y_STATS))

        #On itère à travers la file d'individus pour afficher chacun d'entre eux
        #Note : chaque individu sait lui-même se dessiner, on a donc juste a appeler leur propre fonction Afficher
        for individu in liste:
            individu.Afficher(fenetre)
   


        #Suite de la fonction pour afficher les textes, tout ça est séparé dans une fonction annexe pour pas polluer 
        # self.__Affichage_Ecriture(fenetre)
        
    def Nouveau_tour(self):
        
        for individu in liste:
            if not individu.alive:
                liste.retirer(individu)
        
        


    
    




