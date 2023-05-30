import pygame, constantes, stockage, stats
from Simulation import *


class Button():
    
    def __init__(self, x, y, chemin_image):
        self.x = x
        self.y = y
        
        if chemin_image == "assets/start_bouton.png":
            self.image = pygame.transform.scale(pygame.image.load(chemin_image), (constantes.LARGEUR_BOUTON_START, constantes.HAUTEUR_BOUTON_START))
        elif chemin_image == "assets/plus_bouton.png":
            self.image = pygame.transform.scale(pygame.image.load(chemin_image), (constantes.LARGEUR_BOUTON_PLUS, constantes.HAUTEUR_BOUTON_PLUS))
        elif chemin_image == "assets/moins_bouton.png":
            self.image = pygame.transform.scale(pygame.image.load(chemin_image), (constantes.LARGEUR_BOUTON_MOINS, constantes.HAUTEUR_BOUTON_MOINS))
        elif chemin_image =="assets/bouton_clear.png":
            self.image = pygame.transform.scale(pygame.image.load(chemin_image), (constantes.LARGEUR_BOUTON_CLEAR, constantes.HAUTEUR_BOUTON_CLEAR))
        
        self.rect = self.image.get_rect()
    
    # Affiche le bouton en question
    def Afficher(self, fenetre):
        fenetre.blit(self.image, (self.x, self.y))

# Fonction qui vérifie si le clic est effectué sur le bouton passé en paramètre
def check_souris(bouton):
    mouse = pygame.mouse.get_pos()
    # On cherche de quel bouton il s'agit
    if bouton == "bouton_start":
        if (mouse[0] >= constantes.x_bouton_start_fenetre and mouse[0] <= constantes.x_bouton_start_fenetre + constantes.LARGEUR_BOUTON_START) and (mouse[1] >= constantes.y_bouton_start_fenetre and mouse[1] <= constantes.y_bouton_start_fenetre + constantes.HAUTEUR_BOUTON_START):
            return True
    elif bouton == "bouton_moins_nb_individus":
        if (mouse[0] >= constantes.x_bouton_moins_individus_fenetre and mouse[0] <= constantes.x_bouton_moins_individus_fenetre + constantes.LARGEUR_BOUTON_MOINS) and (mouse[1] >= constantes.y_bouton_moins_individus_fenetre and mouse[1] <= constantes.y_bouton_moins_individus_fenetre + constantes.HAUTEUR_BOUTON_MOINS):
            return True
    elif bouton == "bouton_plus_nb_individus":
        if (mouse[0] >= constantes.x_bouton_plus_individus_fenetre and mouse[0] <= constantes.x_bouton_plus_individus_fenetre + constantes.LARGEUR_BOUTON_PLUS) and (mouse[1] >= constantes.y_bouton_plus_individus_fenetre and mouse[1] <= constantes.y_bouton_plus_individus_fenetre + constantes.HAUTEUR_BOUTON_PLUS):
            return True
    elif bouton == "bouton_moins_food":
        if (mouse[0] >= constantes.x_bouton_moins_food_fenetre and mouse[0] <= constantes.x_bouton_moins_food_fenetre + constantes.LARGEUR_BOUTON_MOINS) and (mouse[1] >= constantes.y_bouton_moins_food_fenetre and mouse[1] <= constantes.y_bouton_moins_food_fenetre + constantes.HAUTEUR_BOUTON_MOINS):
            return True
    elif bouton == "bouton_plus_food":
        if (mouse[0] >= constantes.x_bouton_plus_food_fenetre and mouse[0] <= constantes.x_bouton_plus_food_fenetre + constantes.LARGEUR_BOUTON_PLUS) and (mouse[1] >= constantes.y_bouton_plus_food_fenetre and mouse[1] <= constantes.y_bouton_plus_food_fenetre + constantes.HAUTEUR_BOUTON_PLUS):
            return True
    elif bouton == "bouton_moins_time":
        if (mouse[0] >= constantes.x_bouton_moins_time_fenetre and mouse[0] <= constantes.x_bouton_moins_time_fenetre + constantes.LARGEUR_BOUTON_MOINS) and (mouse[1] >= constantes.y_bouton_moins_time_fenetre and mouse[1] <= constantes.y_bouton_moins_time_fenetre + constantes.HAUTEUR_BOUTON_MOINS):
            return True
    elif bouton == "bouton_plus_time":
        if (mouse[0] >= constantes.x_bouton_plus_time_fenetre and mouse[0] <= constantes.x_bouton_plus_time_fenetre + constantes.LARGEUR_BOUTON_PLUS) and (mouse[1] >= constantes.y_bouton_plus_time_fenetre and mouse[1] <= constantes.y_bouton_plus_time_fenetre + constantes.HAUTEUR_BOUTON_PLUS):
            return True
    elif bouton == "bouton_clear":
        if (mouse[0] >= constantes.x_bouton_clear_fenetre and mouse[0] <= constantes.x_bouton_clear_fenetre + constantes.LARGEUR_BOUTON_CLEAR) and (mouse[1] >= constantes.y_bouton_clear_fenetre and mouse[1] <= constantes.y_bouton_clear_fenetre + constantes.HAUTEUR_BOUTON_CLEAR):
            return True
    else:
        return False
            
        # morceau de code pour tester si ça marche
        # if mouse[0] >= 0 and mouse[1] >= 0:
        #     return True
        # else:
        #     return False

def texte_timer(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    # Chargement de la police
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE + 8)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("{}".format(stockage.timer), True, couleur_texte)
    # Position du texte
    position_texte = ((0.85*constantes.LARGEUR_SETTINGS), (0.1*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)   

def texte_generation(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    # Chargement de la police
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("generation : 0", True, couleur_texte)
    # Position du texte
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.05*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)
    
def texte_nb_individus(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    # Chargement de la police
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("individus : {} ".format(stockage.nb_individus), True, couleur_texte)
    # Position du texte
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.05*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_facteur_food(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("facteur food: {} ".format(stockage.facteur_food), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.2*constantes.HAUTEUR_SETTINGS ))
    fenetre.blit(texte_generation, position_texte)

def texte_tableur(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("tableur:", True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.4*constantes.HAUTEUR_SETTINGS ))
    fenetre.blit(texte_generation, position_texte)

def texte_time_generation(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("time génération: {} s".format(stockage.time_generation), True, couleur_texte)
    position_texte = ((0.35*constantes.LARGEUR_SETTINGS), (0.05*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_individus_start(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("nombre individus départ: {}".format(stats.nb_individus_start), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.15*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_individus_alive(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("nombre individus en vie: {}".format(stats.nb_individus_alive), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.25*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_birth(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("nombre naissances: {}".format(stats.births), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.35*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_individus_dead(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("nombre de morts: {}".format(stats.nb_individus_dead), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.45*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_individu_dead_total(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("nombre individus morts total: {}".format(stats.nb_individus_dead_total), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.55*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_moyenne_size(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("moyenne taille individus: {}".format(stats.individus_moyenne_size), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.65*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_moyenne_view(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("moyenne champ de vision individus: {}".format(stats.individus_moyenne_view), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.75*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)

def texte_moyenne_speed(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("moyenne speed individus: {}".format(stats.individus_moyenne_speed), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.85*constantes.HAUTEUR_SETTINGS))
    fenetre.blit(texte_generation, position_texte)
    
def texte_status(fenetre):
    # Couleur du texte (blanc)
    couleur_texte = (255, 255, 255)
    police = pygame.font.Font(None, constantes.POLICE_ECRITURE)  # None spécifie la police par défaut, 36 est la taille de la police
    # Création de l'objet texte
    texte_generation = police.render("statut simulation: {}".format(stats.statut), True, couleur_texte)
    position_texte = ((0.05*constantes.LARGEUR_SETTINGS), (0.5*constantes.HAUTEUR_SETTINGS ))
    fenetre.blit(texte_generation, position_texte)

# Ecran affiché avant la création de l'objet simulation, permet donc l'affichage sans la fonction Afficher de l'objet simulation
def ecran_avant_début(fenetre):
    # On commence par effacer l'écran de la frame précédante en coloriant l'écran
    fenetre.fill("white")
                
    # On crée les différentes surfaces
    surface_general = pygame.Surface((constantes.LARGEUR_GENERAL, constantes.HAUTEUR_GENERAL)) # dimensions (largeur-hauteur)
    surface_settings = pygame.Surface((constantes.LARGEUR_SETTINGS, constantes.HAUTEUR_SETTINGS))
    surface_stats = pygame.Surface((constantes.LARGEUR_STATS, constantes.HAUTEUR_STATS))
    
    # On leur donne des couleurs
    surface_general.fill("black")  # couleur noire
    surface_stats.fill((0, 133, 31))  # couleur verte
    surface_settings.fill("blue")  # couleur bleu 

    # Affichage des boutons
    image = pygame.transform.scale(pygame.image.load("assets/start_bouton.png"), (constantes.LARGEUR_BOUTON_START, constantes.HAUTEUR_BOUTON_START))
    surface_settings.blit(image, (constantes.x_bouton_start_settings, constantes.y_bouton_start_settings))

    image = pygame.transform.scale(pygame.image.load("assets/moins_bouton.png"), (constantes.LARGEUR_BOUTON_MOINS, constantes.HAUTEUR_BOUTON_MOINS))
    surface_settings.blit(image, (constantes.x_bouton_moins_individus_settings, constantes.y_bouton_moins_individus_settings))
        
    image = pygame.transform.scale(pygame.image.load("assets/plus_bouton.png"), (constantes.LARGEUR_BOUTON_PLUS, constantes.HAUTEUR_BOUTON_PLUS))
    surface_settings.blit(image, (constantes.x_bouton_plus_individus_settings, constantes.y_bouton_plus_individus_settings))
    
    image = pygame.transform.scale(pygame.image.load("assets/moins_bouton.png"), (constantes.LARGEUR_BOUTON_MOINS, constantes.HAUTEUR_BOUTON_MOINS))
    surface_settings.blit(image, (constantes.x_bouton_moins_food_settings, constantes.y_bouton_moins_food_settings))
        
    image = pygame.transform.scale(pygame.image.load("assets/plus_bouton.png"), (constantes.LARGEUR_BOUTON_PLUS, constantes.HAUTEUR_BOUTON_PLUS))
    surface_settings.blit(image, (constantes.x_bouton_plus_food_settings, constantes.y_bouton_plus_food_settings))

    image = pygame.transform.scale(pygame.image.load("assets/moins_bouton.png"), (constantes.LARGEUR_BOUTON_MOINS, constantes.HAUTEUR_BOUTON_MOINS))
    surface_settings.blit(image, (constantes.x_bouton_moins_time_settings, constantes.y_bouton_moins_time_settings))
        
    image = pygame.transform.scale(pygame.image.load("assets/plus_bouton.png"), (constantes.LARGEUR_BOUTON_PLUS, constantes.HAUTEUR_BOUTON_PLUS))
    surface_settings.blit(image, (constantes.x_bouton_plus_time_settings, constantes.y_bouton_plus_time_settings))

    image = pygame.transform.scale(pygame.image.load("assets/bouton_clear.png"), (constantes.LARGEUR_BOUTON_CLEAR, constantes.HAUTEUR_BOUTON_CLEAR))
    surface_settings.blit(image, (constantes.x_bouton_clear_settings, constantes.y_bouton_clear_settings))

    # On appelle toutes ces fonctions pour les afficher sur l'écran
    texte_generation(surface_stats)
    texte_nb_individus(surface_settings)
    texte_facteur_food(surface_settings)
    texte_tableur(surface_settings)
    texte_time_generation(surface_settings)
    texte_timer(surface_settings)
    texte_moyenne_size(surface_stats)
    texte_moyenne_view(surface_stats)
    texte_moyenne_speed(surface_stats)
    texte_individus_start(surface_stats)
    texte_individus_alive(surface_stats)
    texte_birth(surface_stats)
    texte_individus_dead(surface_stats)
    texte_individu_dead_total(surface_stats)
    texte_status(surface_settings)

    # On injecte les surfaces sur l'écran
    fenetre.blit(surface_general, (constantes.X_GENERAL, constantes.Y_GENERAL)) # coordonnées (x, y)
    fenetre.blit(surface_settings, (constantes.X_SETTINGS, constantes.Y_SETTINGS))
    fenetre.blit(surface_stats, (constantes.X_STATS, constantes.Y_STATS))
    
    pygame.display.flip()

	
