import os
os.chdir("natural_selection_sim-main/")
import pygame, constantes
from queue import *
from Simulation import *
from UI import *


facteur_food = 100 # facteur de nourriture


class App:
    def __init__(self) -> None:
        # On va faire 20 frames à chaque seconde (20 FPS), donc la boucle principale est répétée 20 fois à chaque seconde
        self.FPS = 20 # 20 fps recommandé
        self.lecture = True
        self.pause = True # Pour ne pas commencer tout de suite la simulation
        
        #Initialisation de pygame et de la fenêtre
        pygame.init()
        pygame.display.set_caption("Simulation de la vie")
        self.screen = pygame.display.set_mode((constantes.largeur, constantes.hauteur)) # On importe les valeurs récupérées dans le fichier constantes
        
        
        self.chrono = pygame.time.Clock()

        # Création des boutons
        self.bouton_start = Button(constantes.x_bouton_start_settings, constantes.y_bouton_start_settings, "assets/start_bouton_troll.png")
        self.bouton_plus_individus = Button(constantes.x_bouton_plus_individus_settings, constantes.y_bouton_plus_individus_settings, "assets/plus_bouton.png")
        self.bouton_moins_individus = Button(constantes.x_bouton_moins_individus_settings, constantes.y_bouton_moins_individus_settings, "assets/moins_bouton.png")
        
    # Boucle principale du programme
    def main(self) -> None:
        
        self.simulation = Simulation(queue.nb_individus, facteur_food)
        
        # On fait 15 secondes par tours, 20 * 15 soit 300 boucles par tour, avant de passer à un nouveau tour         
        while self.lecture:
            
            while self.pause == True:
                self.Demande_Evenements()
                ecran_avant_début(self.screen)
        
            
            for _ in range(self.FPS * 15): # Pour chaque frame d'un tour
                while self.pause:
                    # Si le jeu est en pause il faut quand même vérifier si l'utilisateur rappuie sur pause ou sur quitter
                    if not self.lecture: break
                    self.Demande_Evenements()
                    # Et il faut quand même que la fenêtre soit fluide, sinon on a l'impression que le jeu a planté
                    pygame.display.flip()
                    self.chrono.tick(self.FPS)

                if not self.lecture: break

                # Les 3 fonctions les plus importantes de ce programme : elles sont appelées successivement à chaque frame
                # 1) On gère les appuis de touches de clavier (évenements) à partir de la liste d'évenements donnée par pygame
                # 2) On actualise la simulation et chaque individu
                # 3) On affiche tous les éléments graphiques
                
                self.Demande_Evenements()
                self.simulation.Mise_A_Jour()
                self.simulation.Afficher(self.screen)
                
                self.bouton_start.Afficher(self.simulation.surface_settings)
                self.bouton_plus_individus.Afficher(self.simulation.surface_settings)
                self.bouton_moins_individus.Afficher(self.simulation.surface_settings)

                # pygame.display.flip() doit être appelée à chaque frame pour actualiser la fenêtre
                pygame.display.flip()
                
                # On limite le nombre d'itérations par seconde à 20 grâce à pygame
                self.chrono.tick(self.FPS)
            else:
                # C'est une boucle for-else, ce else se déclenche uniquement si aucun "break" n'a été déclenché
                # Après 15 secondes, on démarre un nouveau tour, naissances, morts, apparition de nourriture
                self.simulation.Nouveau_tour(facteur_food)

        # On arrive ici uniquement si l'utilisateur souhaite quitter le programme, donc on ferme pygame
        pygame.quit()

    def Demande_Evenements(self) -> list:
        # Cette fonction vérifie si l'utilisateur veut fermer la fenêtre, et obtient la liste d'évenements qui sera transmise à la suite du programme
        
        #rep est une liste d'évenements, à chaque frame pygame va y mettre toutes les interactions avec l'utilisateur
        rep:list = pygame.event.get()

        # On itère sur la liste pour vérifier si il y a un élément qui nous intéresse
        for event in rep:
            # Si l'utilisateur appuie sur la touche ECHAP, quitte la simulation
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.lecture = False
                break
            # Si l'utilisateur appuie sur le bouton start
            if event.type == pygame.MOUSEBUTTONDOWN and check_souris("bouton_start") == True:
                # self.lecture = True
                self.pause = not self.pause
                break
            # Si l'utilisateur appuie sur le bouton plus individus
            if event.type == pygame.MOUSEBUTTONDOWN and check_souris("bouton_plus_nb_individus") == True:
                
                self.pause = not self.pause
                break
            # Si l'utilisateur appuie sur le bouton moins individus
            if event.type == pygame.MOUSEBUTTONDOWN and check_souris("bouton_moins_nb_individus") == True:
                # self.lecture = True
                self.pause = not self.pause
                break
            # Si l'utilisateur appuie sur la touche p, met la simualtion en pause
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.pause = not self.pause
                break
        # return rep
    
    
run = App()
run.main()