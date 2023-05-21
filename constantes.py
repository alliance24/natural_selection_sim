import pygame
pygame.init()

# On récupère les dimensions de l'écran
infos = pygame.display.Info()
largeur = infos.current_w
hauteur = infos.current_h

# On utilise des facteurs pour que les fenêtres soient adaptatives en fonction de l'écran
LARGEUR_GENERAL = 0.98*hauteur
HAUTEUR_GENERAL = 0.98*hauteur
X_GENERAL = 0.01*hauteur
Y_GENERAL = 0.01*hauteur


LARGEUR_SETTINGS = largeur-hauteur*1.01 
HAUTEUR_SETTINGS = 0.48*hauteur
X_SETTINGS = hauteur
Y_SETTINGS = 0.01*hauteur


LARGEUR_STATS = largeur-hauteur*1.01
HAUTEUR_STATS = 0.48*hauteur
X_STATS = hauteur
Y_STATS = 0.51*hauteur

# Tailles
TAILLE_FOOD = 12