import pygame, constantes, queue
from stats import *
from UI import *
from Creature import *
from class_food import *

class Simulation:
    def __init__(self, nb_creature, facteur_food):
        self.generation = 1 # Numéro de tour (commence donc à 1)
        self.stats = Statistiques()
        
        self.nb_creature = nb_creature
        self.facteur_food = facteur_food
        
        for individu in range(nb_creature):
            individu = Creature(self.generation)
            queue.liste_individus.append(individu)
        
        for e in range(int((self.facteur_food*nb_creature)/100)):
                e = Food()
                queue.liste_food.append(e)
        
        
    def Mise_A_Jour(self) -> None:
        # Ce qui est différent d'une frame à l'autre; toutes les actualisations se font ici
        # print("------------------------------------------------------------------------------")
        for individu in queue.liste_individus:
            if individu.alive == True:
                # print("---------------------------")
                # print(individu.x, individu.y)
                individu.move()
                # print(individu.x, individu.y)
                # print("---------------------------")
                # print(individu.rect)
                for food in queue.liste_food:
                    if food.eat == False:
                        # print(food.x, food.y)
                        if individu.eat(food.get_x(), food.get_y()):
                            food.eat = True
    
    def texte_generation(self, fenetre):
        # generations
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        # Chargement de la police
        police = pygame.font.Font(None, 36)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("generation : {}".format(self.generation), True, couleur_texte)
        # Position du texte
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.05*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    
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
        self.surface_stats.fill((0, 133, 31))  # couleur verte
        self.surface_settings.fill("blue")  # couleur bleu
        
        
        
        # On injecte la nourriture sur l'écran
        for food in queue.liste_food:
            if food.eat == False:
                food.Afficher(self.surface_general)
        
        # On injecte les individus sur l'écran
        for individu in queue.liste_individus:
            if individu.alive == True:
                individu.Afficher(self.surface_general)   
        
        # Affiche les textes (comme le numéro de la génération)
        self.texte_generation(self.surface_stats)
        
        # On injecte les surfaces sur l'écran
        fenetre.blit(self.surface_stats, (constantes.X_STATS, constantes.Y_STATS))    
        fenetre.blit(self.surface_general, (constantes.X_GENERAL, constantes.Y_GENERAL)) # coordonnées (x, y)
        fenetre.blit(self.surface_settings, (constantes.X_SETTINGS, constantes.Y_SETTINGS))

        
        
    def Nouveau_tour(self, facteur_food):
        
        self.generation += 1
        
        queue.liste_food.clear() # On réinitialise la nourriture
        
        # On tue des individus
        for individu in queue.liste_individus:
            if individu.food < 1:
                individu.alive = False
            if not individu.alive:
                queue.liste_individus.remove(individu)
        
        nb_indiv_alive = len(queue.liste_individus) # Compteur des individus vivants après la génération
        
        # On regénère des individus
        for individu in queue.liste_individus:
            if individu.food >= 2:
                queue.liste_individus.append(Creature(self.generation))
                self.stats.births += 1
                
        
        for e in range(int((facteur_food*nb_indiv_alive)/100)): # On regénère de la nourriture en fonction du nb d'individus vivants et du facteur
                e = Food()
                queue.liste_food.append(e)
        
        
        


    
    




