import os
os.chdir("natural_selection_sim-main/")
import pygame, constantes, queue
from stats import *
from Simulation import *
import queue


nb_individu = 15
facteur_food = 1000 # facteur de nourriture

class App:
    def __init__(self) -> None:
        #On va faire 60 frames à chaque seconde (60 FPS), donc la boucle principale est répétée 60 fois à chaque seconde
        self.FPS = 60
        self.lecture = True
        self.pause = False

        #Initialisation de pygame et de la fenêtre
        pygame.init()
        pygame.display.set_caption("Simulation de la vie")
        self.screen = pygame.display.set_mode((constantes.largeur, constantes.hauteur)) # On importe les valeurs récupérées dans le fichier constantes
        
        self.stats = Statistiques()
        self.food = facteur_food
        self.simulation = Simulation(nb_individu)
        self.chrono = pygame.time.Clock()
        
    #Boucle principale du programme
    def main(self) -> None:
        
        for e in range(int((self.food*nb_individu)/100)):
                e = Food()
                queue.liste_food.append(e)
        
        
        #On fait 10 secondes par tours, 60 * 10 soit 600 boucles par tour, avant de passer à un nouveau tour         
        while self.lecture:
            count = 1
            self.stats.individus_per_round[count-1].append(count)
            
            
            for _ in range(self.FPS * 10): # Pour chaque frame d'un tour
                while self.pause:
                    #Si le jeu est en pause il faut quand même vérifier si l'utilisateur rappuie sur pause ou sur quitter
                    if not self.lecture: break
                    self.Demande_Evenements()
                    #Et il faut quand même que la fenêtre soit fluide, sinon on a l'impression que le jeu a planté
                    pygame.display.flip()
                    self.chrono.tick(self.FPS)

                if not self.lecture: break

                #Les 3 fonctions les plus importantes de ce programme : elles sont appelées successivement à chaque frame
                # 1) On gère les appuis de touches de clavier (évenements) à partir de la liste d'évenements donnée par pygame
                # 2) On actualise le monde et chaque individu, tous les calculs et décisions sont faites là
                # 3) On affiche tous les éléments graphiques (individus, rects, textes..)
                
                self.Demande_Evenements()
                self.simulation.Mise_A_Jour()
                self.simulation.Afficher(self.screen)

                # pygame.display.flip() doit être appelée à chaque frame pour actualiser la fenêtre
                pygame.display.flip()
                # On limite le nombre d'itérations par seconde à 60 grâce à pygame
                self.chrono.tick(self.FPS)
            # else:
            #     # C'est une boucle for-else, ce else se déclenche uniquement si aucun "break" n'a été déclenché
            #     # Après 10 secondes, on démarre un nouveau tour, naissances, morts, apparition de nourriture
            #     self.monde.Nouvelle_Generation()

        #On arrive ici uniquement si l'utilisateur souhaite quitter le programme, donc on ferme pygame
        pygame.quit()

    def Demande_Evenements(self) -> list:
        #Cette fonction vérifie si l'utilisateur veut fermer la fenêtre, et obtient la liste d'évenements qui sera transmise à la suite du programme
        
        #rep est une liste d'évenements, à chaque frame pygame va y mettre toutes les interactions avec l'utilisateur
        rep:list = pygame.event.get()

        # On itère sur la liste pour vérifier si il y a un élément qui nous intéresse
        for event in rep:
            # Si l'utilisateur appuie sur la touche ECHAP, quitte la simulation
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.lecture = False
                break
            # Si l'utilisateur appuie sur la touche p, met la simualtion en pause
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.pause = not self.pause
                break

        # #On retransmet cette liste d'évenements au monde qui pourra itérer aussi
        # return rep
    
    
run = App()
run.main()

