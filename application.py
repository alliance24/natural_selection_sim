import os
os.chdir("natural_selection_sim-main/")
import pygame, constantes, UI, queue, stats, export
from plyer import notification
from Simulation import *


class App:
    
    def __init__(self):
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
        self.bouton_start = UI.Button(constantes.x_bouton_start_settings, constantes.y_bouton_start_settings, "assets/start_bouton.png")
        self.bouton_plus_individus = UI.Button(constantes.x_bouton_plus_individus_settings, constantes.y_bouton_plus_individus_settings, "assets/plus_bouton.png")
        self.bouton_moins_individus = UI.Button(constantes.x_bouton_moins_individus_settings, constantes.y_bouton_moins_individus_settings, "assets/moins_bouton.png")
        self.bouton_moins_food = UI.Button(constantes.x_bouton_moins_food_settings, constantes.y_bouton_moins_food_settings,"assets/moins_bouton.png")
        self.bouton_plus_food = UI.Button(constantes.x_bouton_plus_food_settings, constantes.y_bouton_plus_food_settings,"assets/plus_bouton.png")
        self.bouton_moins_time = UI.Button(constantes.x_bouton_moins_time_settings, constantes.y_bouton_moins_time_settings,"assets/moins_bouton.png")
        self.bouton_clear = UI.Button(constantes.x_bouton_clear_settings, constantes.y_bouton_clear_settings, "assets/bouton_clear.png")
        
    # Boucle principale du programme
    def main(self):
        
        global supp
        
        while self.pause == True:
            self.Demande_Evenements()
            UI.ecran_avant_début(self.screen)
        
        # Prépare pour l'export des statistiques
        if supp == "y":
            export.clear()
        else:
            export.create_sheet()
        export.load_and_write()
        
        stats.statut = "En cours"
        stats.nb_individus_start = queue.nb_individus
        self.simulation = Simulation(queue.nb_individus, queue.facteur_food)
        queue.timer = queue.time_generation
        
        # On fait n secondes par tours, 20 * n soit 20 * n boucles par tour, avant de passer à un nouveau tour         
        while self.lecture:
            
            for _ in range(self.FPS * queue.time_generation): # Pour chaque frame d'un tour

                while self.pause:
                    
                    # Si le jeu est en pause il faut quand même vérifier si l'utilisateur rappuie sur pause ou sur quitter
                    if not self.lecture: break
                    self.Demande_Evenements()
                    # Et il faut quand même que la fenêtre soit fluide, sinon on a l'impression que le jeu a planté
                    pygame.display.flip()
                    self.chrono.tick(self.FPS)

                if not self.lecture: break
                
                # Les 3 fonctions les plus importantes de ce programme : elles sont appelées successivement à chaque frame
                # 1) On gère les appuis de touches claviers ainsi que les boutons à partir de la liste d’évènements donnée par pygame
                # 2) On actualise la simulation et chaque individu
                # 3) On affiche tous les éléments graphiques
                
                queue.nb_boucles-=1
                if queue.nb_boucles %20 == 0: # Il y a 20 FPS pour n nombre de seconde donc on regarde si le nombre est multiple de 20 pour retirer 1 seconde au timer
                    queue.timer-=1      
                              
                self.Demande_Evenements()
                self.simulation.Mise_A_Jour()
                self.simulation.Afficher(self.screen)

                # pygame.display.flip() doit être appelée à chaque frame pour actualiser la fenêtre
                pygame.display.flip()
                
                # On limite le nombre d'itérations par seconde à 20 grâce à pygame
                self.chrono.tick(self.FPS)
            else:
                queue.timer= queue.time_generation
                # C'est une boucle for-else, ce else se déclenche uniquement si aucun "break" n'a été déclenché
                # Après 15 secondes, on démarre un nouveau tour, naissances, morts, apparition de nourriture
                if self.simulation.Nouveau_tour(queue.facteur_food) == False:
                    stats.statut = "Terminé"
                    # export.graph()
                    notification.notify( # Notification windows
                        title='Simulation',
                        message='Fin de la simulation',
                        timeout=10 
                        )

                    while True:
                        self.Demande_Evenements_END()
                        self.simulation.Afficher(self.screen)
                        pygame.display.flip()           

        # On arrive ici uniquement si l'utilisateur souhaite quitter le programme, donc on ferme pygame
        pygame.quit()

    def Demande_Evenements(self):
        # Cette fonction vérifie si l'utilisateur veut fermer la fenêtre, et obtient la liste d'évenements qui sera transmise à la suite du programme
        
        global supp
        
        #rep est une liste d'évenements, à chaque frame pygame va y mettre toutes les interactions avec l'utilisateur
        rep:list = pygame.event.get()

        # On itère sur la liste pour vérifier si il y a un élément qui nous intéresse
        for event in rep:
            # Si l'utilisateur appuie sur la touche ECHAP, quitte la simulation
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.lecture = False
                break
            # Si l'utilisateur appuie sur le bouton start
            if event.type == pygame.MOUSEBUTTONDOWN and UI.check_souris("bouton_start") == True:
                # self.lecture = True
                self.pause = not self.pause
                break
            # Si l'utilisateur appuie sur le bouton plus individus
            if event.type == pygame.MOUSEBUTTONDOWN and UI.check_souris("bouton_plus_nb_individus") == True:
                queue.nb_individus += 1
            # Si l'utilisateur appuie sur le bouton moins individus
            if event.type == pygame.MOUSEBUTTONDOWN and UI.check_souris("bouton_moins_nb_individus") == True:
                if queue.nb_individus>0:
                    queue.nb_individus -= 1
            if event.type == pygame.MOUSEBUTTONDOWN and UI.check_souris("bouton_moins_food"):
                if queue.facteur_food >= 5:
                    queue.facteur_food -= 5
            if event.type == pygame.MOUSEBUTTONDOWN and UI.check_souris("bouton_plus_food"):
                queue.facteur_food += 5
            if event.type == pygame.MOUSEBUTTONDOWN and UI.check_souris("bouton_moins_time"):
                if queue.time_generation>0:
                    queue.time_generation -=1   
            if event.type == pygame.MOUSEBUTTONDOWN and UI.check_souris("bouton_plus_time"):
                queue.time_generation +=1
            if event.type == pygame.MOUSEBUTTONDOWN and UI.check_souris("bouton_clear"):
                supp = "y"
            # Si l'utilisateur appuie sur la touche p, met la simualtion en pause
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.pause = not self.pause
                break
        # return rep
        
    def Demande_Evenements_END(self):
        rep:list = pygame.event.get()

        # On itère sur la liste pour vérifier si il y a un élément qui nous intéresse
        for event in rep:
            # Si l'utilisateur appuie sur la touche ECHAP, quitte la simulation
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit() 


supp = ""   
run = App()
run.main()