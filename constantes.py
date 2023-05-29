import pygame
pygame.init()

# On récupère les dimensions de l'écran
infos = pygame.display.Info()
largeur = infos.current_w
hauteur = infos.current_h

# On utilise des facteurs pour que les fenêtres soient adaptatives en fonction de l'écran
# Surface_general
LARGEUR_GENERAL = 0.98*hauteur
HAUTEUR_GENERAL = 0.98*hauteur
X_GENERAL = 0.01*hauteur
Y_GENERAL = 0.01*hauteur

# Surface_settings
LARGEUR_SETTINGS = largeur-hauteur*1.01 
HAUTEUR_SETTINGS = 0.48*hauteur
X_SETTINGS = hauteur
Y_SETTINGS = 0.01*hauteur

# Surface_stats
LARGEUR_STATS = largeur-hauteur*1.01
HAUTEUR_STATS = 0.48*hauteur
X_STATS = hauteur
Y_STATS = 0.51*hauteur

# Tailles
TAILLE_FOOD = 12
POLICE_ECRITURE = 36

# ---------------------------------------------------------------------------------------------------------
LARGEUR_BOUTON_START = 100
HAUTEUR_BOUTON_START = 50
# ---------------------------------------------------------------------------------------------------------
LARGEUR_BOUTON_MOINS = 25
HAUTEUR_BOUTON_MOINS = 25
# ---------------------------------------------------------------------------------------------------------
LARGEUR_BOUTON_PLUS = 25
HAUTEUR_BOUTON_PLUS = 25
# ---------------------------------------------------------------------------------------------------------


# Positions relatives des boutons

# ---------------------------------------------------------------------------------------------------------
# Bouton START
# x par rapport aux settings: ((largeur_fenetre-hauteur_fenetre*1.01)-largeur_bouton)/2
# x par rapport à la fenêtre: x surface_settings + x par rapport aux settings
x_bouton_start_settings = ((largeur-hauteur*1.01)-LARGEUR_BOUTON_START)/2
x_bouton_start_fenetre = X_SETTINGS + x_bouton_start_settings


# y par rapport aux settings: ((0.48*hauteur_fenetre)*0.9)-hauteur_bouton
# y par rapport à la fenêtre: y surface_settings + y par rapport aux settings
y_bouton_start_settings = ((0.48*hauteur)*0.9)-HAUTEUR_BOUTON_START
y_bouton_start_fenetre = Y_SETTINGS + y_bouton_start_settings

# ---------------------------------------------------------------------------------------------------------
#bouton moins individu 
# x par rapport aux settings: ((largeur_fenetre-hauteur_fenetre*1.01)-largeur_bouton)/2
# x par rapport à la fenêtre: x surface_settings + x par rapport aux settings
x_bouton_moins_individus_settings = (0.1*HAUTEUR_SETTINGS)
x_bouton_moins_individus_fenetre = X_SETTINGS + x_bouton_moins_individus_settings


# y par rapport aux settings: ((0.48*hauteur_fenetre)*0.9)-hauteur_bouton
# y par rapport à la fenêtre: y surface_settings + y par rapport aux settings
y_bouton_moins_individus_settings = (0.075*LARGEUR_SETTINGS)
y_bouton_moins_individus_fenetre = Y_SETTINGS + y_bouton_moins_individus_settings

# ---------------------------------------------------------------------------------------------------------
#bouton plus individu
# x par rapport aux settings: ((largeur_fenetre-hauteur_fenetre*1.01)-largeur_bouton)/2
# x par rapport à la fenêtre: x surface_settings + x par rapport aux settings
x_bouton_plus_individus_settings = x_bouton_moins_individus_settings*2 + LARGEUR_BOUTON_PLUS
x_bouton_plus_individus_fenetre = X_SETTINGS + x_bouton_plus_individus_settings


# y par rapport aux settings: ((0.48*hauteur_fenetre)*0.9)-hauteur_bouton
# y par rapport à la fenêtre: y surface_settings + y par rapport aux settings
y_bouton_plus_individus_settings = (0.075*LARGEUR_SETTINGS)
y_bouton_plus_individus_fenetre = Y_SETTINGS + y_bouton_plus_individus_settings

# ---------------------------------------------------------------------------------------------------------
#Bouton moins food
# x par rapport aux settings:
# x par rapport à la fenêtre:
x_bouton_moins_food_settings = (0.1*HAUTEUR_SETTINGS)
x_bouton_moins_food_fenetre = X_SETTINGS + x_bouton_moins_food_settings


# y par rapport aux settings:
# y par rapport à la fenêtre:
y_bouton_moins_food_settings = (0.175*LARGEUR_SETTINGS)
y_bouton_moins_food_fenetre = Y_SETTINGS + y_bouton_moins_food_settings

# ---------------------------------------------------------------------------------------------------------
#Bouton plus food
# x par rapport aux settings:
# x par rapport à la fenêtre:
x_bouton_plus_food_settings = x_bouton_moins_food_settings*2 + LARGEUR_BOUTON_MOINS
x_bouton_plus_food_fenetre = X_SETTINGS + x_bouton_plus_food_settings


# y par rapport aux settings:
# y par rapport à la fenêtre:
y_bouton_plus_food_settings = (0.175*LARGEUR_SETTINGS)
y_bouton_plus_food_fenetre = Y_SETTINGS + y_bouton_plus_food_settings 

# ---------------------------------------------------------------------------------------------------------
#bouton moins time génération
# x par rapport aux settings:
# x par rapport à la fenêtre:
x_bouton_moins_time_settings = (0.4*LARGEUR_SETTINGS)
x_bouton_moins_time_fenetre = X_SETTINGS + x_bouton_moins_time_settings



# y par rapport aux settings:
# y par rapport à la fenêtre:
y_bouton_moins_time_settings = (0.075*LARGEUR_SETTINGS)
y_bouton_moins_time_fenetre = Y_SETTINGS + y_bouton_moins_time_settings

# ---------------------------------------------------------------------------------------------------------
#bouton plus time génération
# x par rapport aux settings:
# x par rapport à la fenêtre:
x_bouton_plus_time_settings = (0.55*LARGEUR_SETTINGS)
x_bouton_plus_time_fenetre = X_SETTINGS + x_bouton_plus_time_settings



# y par rapport aux settings:
# y par rapport à la fenêtre:
y_bouton_plus_time_settings = (0.075*LARGEUR_SETTINGS)
y_bouton_plus_time_fenetre = Y_SETTINGS + y_bouton_plus_time_settings