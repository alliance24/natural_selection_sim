import pygame, constantes, queue
from Creature import *
from class_food import *

class Simulation:
    def __init__(self, nb_creature):
        self.nb_creature = nb_creature
        for individu in range(nb_creature):
            individu = Creature()
            queue.liste_individus.append(individu)
        
        
    def Mise_A_Jour(self) -> None:
        # Ce qui est différent d'une frame à l'autre; toutes les actualisations se font ici
        print("------------------------------------------------------------------------------")
        for individu in queue.liste_individus:
            if individu.alive == True:
                print("---------------------------")
                print(individu.x, individu.y)
                individu.move()
                print(individu.x, individu.y)
                # print("---------------------------")
                # print(individu.rect)
                for food in queue.liste_food:
                    if food.eat == False:
                        # print(food.x, food.y)
                        if individu.eat(food.get_x(), food.get_y()):
                            food.eat = True
           
        
    
    def Afficher(self, fenetre) -> None:
        # Une fois que tous les calculs ont été faits dans la fonction Mise_A_Jour, on affiche tous les éléments
        
        # On commence par effacer l'écran de la frame précédante en coloriant l'écran
        fenetre.fill("white")
                    

        # On crée les différentes surfaces
        self.surface_general = pygame.Surface((constantes.LARGEUR_GENERAL, constantes.HAUTEUR_GENERAL)) # dimensions (largeur-hauteur)
        self.surface_settings = pygame.Surface((constantes.LARGEUR_SETTINGS, constantes.HAUTEUR_SETTINGS))
        self.surface_stats = pygame.Surface((constantes.LARGEUR_STATS, constantes.HAUTEUR_STATS))
        
        
        # On leur donne des couleurs
        self.surface_general.fill("black")  # couleur rouge
        self.surface_stats.fill("green")  # couleur verte
        self.surface_settings.fill("blue")  # couleur bleu
        
        # On injecte les surfaces sur l'écran
        fenetre.blit(self.surface_settings, (constantes.X_SETTINGS, constantes.Y_SETTINGS))
        fenetre.blit(self.surface_stats, (constantes.X_STATS, constantes.Y_STATS))
        
        # On injecte la nourriture sur l'écran
        for food in queue.liste_food:
            if food.eat == False:
                food.Afficher(self.surface_general)
        
        # On injecte les individus sur l'écran
        for individu in queue.liste_individus:
            if individu.alive == True:
                individu.Afficher(self.surface_general)   
                    
                
        # On injecte la surface sur l'écran
        fenetre.blit(self.surface_general, (constantes.X_GENERAL, constantes.Y_GENERAL)) # coordonnées (x, y)

        #Suite de la fonction pour afficher les textes, tout ça est séparé dans une fonction annexe pour pas polluer 
        # self.__Affichage_Ecriture(fenetre)
        
    def Nouveau_tour(self):
        
        
        queue.liste_food.clear() # On réinitialise la nourriture
        
        
        for individu in queue.liste_individus:
            if not individu.alive:
                queue.liste_individus.retirer(individu)
        
        nb_indiv_alive = len(queue.liste_individus) # Compteur des individus vivants
        
        for e in range(int((self.food*nb_indiv_alive)/100)): # On regénère de la nourriture en fonction du nb d'individus vivants et du facteur
                e = Food()
                queue.liste_food.append(e)
        
        
        


    
    




