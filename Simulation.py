import pygame, constantes, queue, stats, export
from UI import * 
from Creature import *
from class_food import *

class Simulation:
    def __init__(self, nb_creature, facteur_food):
        stats.generation = 1 # Numéro de tour (commence donc à 1)
        self.facteur_food = facteur_food
        
        for individu in range(nb_creature):
            individu = Creature(stats.generation)
            queue.liste_individus.append(individu)
        
        for e in range(int((self.facteur_food*nb_creature)/100)):
                e = Food()
                queue.liste_food.append(e)
        
        
    def Mise_A_Jour(self) -> None:
        # Ce qui est différent d'une frame à l'autre; toutes les actualisations se font ici
        for individu in queue.liste_individus:
            if individu.alive == True:
                individu.move()
                for food in queue.liste_food:
                    if food.eat == False:
                        if individu.eat(food.get_x(), food.get_y()):
                            food.eat = True

        stats.individus_moyenne_size = stats.moyenne_size()
        stats.individus_moyenne_view = stats.moyenne_view()
        stats.individus_moyenne_speed = stats.moyenne_speed()

    def texte_timer(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        # Chargement de la police
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE + 8)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("{}".format(queue.timer), True, couleur_texte)
        # Position du texte
        position_texte = ((0.85*constantes.LARGEUR_SETTINGS), (0.1*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)   

    def texte_generation(self, fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        # Chargement de la police
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("generation : {}".format(stats.generation), True, couleur_texte)
        # Position du texte
        position_texte = ((0.05*constantes.LARGEUR_STATS), (0.05*constantes.HAUTEUR_STATS))
        fenetre.blit(texte_generation, position_texte)
        
    def texte_nb_individus(self, fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        # Chargement de la police
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("individus : {}".format(queue.nb_individus), True, couleur_texte)
        # Position du texte
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.05*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)
    
    def texte_facteur_food(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("facteur food: {} ".format(queue.facteur_food), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.2*constantes.HAUTEUR_SETTINGS ))
        fenetre.blit(texte_generation, position_texte)

    def texte_time_generation(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("time génération: {} s".format(queue.time_generation), True, couleur_texte)
        position_texte = ((0.35*constantes.LARGEUR_SETTINGS), (0.05*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    def texte_individus_start(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("nombre individus départ: {}".format(stats.nb_individus_start), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.15*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    def texte_individus_alive(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("nombre individus en vie: {}".format(stats.nb_individus_alive), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.25*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    def texte_birth(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("nombre naissance: {}".format(stats.births), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.35*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    def texte_individus_dead(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("nombre de mort: {}".format(stats.nb_individus_dead), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.45*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    def texte_individu_dead_total(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("nombre individus mort total: {}".format(stats.nb_individus_dead_total), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.55*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    def texte_moyenne_size(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("moyenne taille individus: {}".format(stats.individus_moyenne_size), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.65*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    def texte_moyenne_view(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("moyenne champ de vision individus: {}".format(stats.individus_moyenne_view), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.75*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    def texte_moyenne_speed(self,fenetre):
        # Couleur du texte (blanc)
        couleur_texte = (255, 255, 255)
        police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
        # Création de l'objet texte
        texte_generation = police.render("moyenne speed individus: {}".format(stats.individus_moyenne_speed), True, couleur_texte)
        position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.85*constantes.HAUTEUR_SETTINGS))
        fenetre.blit(texte_generation, position_texte)

    # Une fois que tous les calculs ont été faits dans la fonction Mise_A_Jour, on affiche tous les éléments
    def Afficher(self, fenetre) -> None:
        
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
        
        # Affiche les textes
        self.texte_timer(self.surface_settings)
        self.texte_generation(self.surface_stats)
        self.texte_nb_individus(self.surface_settings)
        self.texte_facteur_food(self.surface_settings)
        self.texte_time_generation(self.surface_settings)
        self.texte_moyenne_size(self.surface_stats)
        self.texte_moyenne_view(self.surface_stats)
        self.texte_moyenne_speed(self.surface_stats)
        self.texte_individus_start(self.surface_stats)
        self.texte_individus_alive(self.surface_stats)
        self.texte_birth(self.surface_stats)
        self.texte_individus_dead(self.surface_stats)
        self.texte_individu_dead_total(self.surface_stats)
        # On injecte les surfaces sur l'écran
        fenetre.blit(self.surface_stats, (constantes.X_STATS, constantes.Y_STATS))    
        fenetre.blit(self.surface_general, (constantes.X_GENERAL, constantes.Y_GENERAL)) # coordonnées (x, y)
        fenetre.blit(self.surface_settings, (constantes.X_SETTINGS, constantes.Y_SETTINGS)) 
    
    # Toute les étapes qui doivent se dérouler après une génération ainsi que le lancement de la suivante
    def Nouveau_tour(self, facteur_food):
        queue.nb_individus = 0
        stats.generation += 1
        stats.individus_moyenne_size = stats.moyenne_size()
        stats.individus_moyenne_view = stats.moyenne_view()
        stats.individus_moyenne_speed = stats.moyenne_speed() 
        queue.liste_food.clear() # On réinitialise la nourriture
        
        # On tue des individus
        stats.nb_individus_dead =0
        stats.births=0    # Reset de se même compteur
        for individu in reversed(queue.liste_individus): # On itère depuis la fin de la liste pour éviter un problème d'indice lors de la suppression des individus
            if individu.food < 1:
                individu.alive = False
                queue.liste_individus.remove(individu)
                stats.nb_individus_dead+=1
                stats.nb_individus_dead_total+=1

        nb_indiv_alive = len(queue.liste_individus) # Compteur des individus vivants après la génération
        
        # On regénère des individus
        for individu in queue.liste_individus:
            if individu.food >= 2:
                queue.liste_individus.append(Creature(stats.generation))
                stats.births += 1

        stats.nb_individus_alive=len(queue.liste_individus)
        
        if stats.nb_individus_alive == 0:
            stats.individus_moyenne_size = 0
            stats.individus_moyenne_view = 0
            stats.individus_moyenne_speed = 0
            export.export()
            return False
        else:
            stats.individus_moyenne_size = stats.moyenne_size()
            stats.individus_moyenne_view = stats.moyenne_view()
            stats.individus_moyenne_speed = stats.moyenne_speed()
            export.export()
        
        # On remet leur niveau de nourriture à 0 et on reactualise la valeur qui contient le nb d'individus
        for individu in queue.liste_individus:
            individu.food = 0
            queue.nb_individus += 1
        
        # On regénère de la nourriture en fonction du nb d'individus vivants et du facteur        
        for e in range(int((facteur_food*nb_indiv_alive)/100)): 
                e = Food()
                queue.liste_food.append(e)

        
        


    
    




