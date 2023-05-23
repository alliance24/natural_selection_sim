import os
os.chdir("natural_selection_sim-main/")

import pygame, constantes
from UI import *

pygame.init()
pygame.display.set_caption("Simulation de la vie")
screen = pygame.display.set_mode((constantes.largeur, constantes.hauteur))

image = pygame.transform.scale(pygame.image.load("assets/start_button_troll.png"), (100, 50))
rect = image.get_rect()

while True:
    
    # On commence par effacer l'écran de la frame précédante en coloriant l'écran
    screen.fill("white")
                

    # On crée les différentes surfaces
    surface_general = pygame.Surface((constantes.LARGEUR_GENERAL, constantes.HAUTEUR_GENERAL)) # dimensions (largeur-hauteur)
    surface_settings = pygame.Surface((constantes.LARGEUR_SETTINGS, constantes.HAUTEUR_SETTINGS))
    surface_stats = pygame.Surface((constantes.LARGEUR_STATS, constantes.HAUTEUR_STATS))
    
    
    # On leur donne des couleurs
    surface_general.fill("black")  # couleur rouge
    surface_stats.fill("green")  # couleur verte
    surface_settings.fill("blue")  # couleur bleu
    
    # On injecte les surfaces sur l'écran
    
    screen.blit(surface_stats, (constantes.X_STATS, constantes.Y_STATS))

    # Button.Afficher(surface_settings)
    surface_settings.blit(image, (365, 450))
        
        
    screen.blit(surface_general, (constantes.X_GENERAL, constantes.Y_GENERAL)) # coordonnées (x, y)
    screen.blit(surface_settings, (constantes.X_SETTINGS, constantes.Y_SETTINGS))
    
    pygame.display.flip()
    
    rep:list = pygame.event.get()

    # On itère sur la liste pour vérifier si il y a un élément qui nous intéresse
    for event in rep:
        # Si l'utilisateur appuie sur la touche ECHAP, quitte la simulation
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            break
        # Si l'utilisateur appuie sur le bouton start
        if event.type == pygame.MOUSEBUTTONDOWN  and check_souris() == True:
            print(True)
            break
        # Si l'utilisateur appuie sur la touche p, met la simualtion en pause
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pygame.quit()
            break
    