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

LARGEUR_BOUTON = 100
HAUTEUR_BOUTON = 50

# Positions relatives du bouton start

# x par rapport aux settings: ((largeur_fenetre-hauteur_fenetre*1.01)-largeur_bouton)/2
# x par rapport à la fenêtre: x surface_settings + x par rapport aux settings
x_bouton_settings = ((largeur-hauteur*1.01)-LARGEUR_BOUTON)/2
x_bouton_fenetre = X_SETTINGS + x_bouton_settings


# y par rapport aux settings: ((0.48*hauteur_fenetre)*0.9)-hauteur_bouton
# y par rapport à la fenêtre: y surface_settings + y par rapport aux settings
y_bouton_settings = ((0.48*hauteur)*0.9)-HAUTEUR_BOUTON
y_bouton_fenetre = Y_SETTINGS + y_bouton_settings