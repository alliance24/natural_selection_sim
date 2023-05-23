import pygame, constantes

class Button():
    def __init__(self, x, y):
        self.etat_click = False
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("assets/start_button_troll.png"), (constantes.LARGEUR_BOUTON, constantes.HAUTEUR_BOUTON))
        self.rect = self.image.get_rect()
    
    def Afficher(self, fenetre):
        fenetre.blit(self.image, (self.x, self.y))

def check_souris(bouton):
        mouse = pygame.mouse.get_pos()
        if (mouse[0] >= constantes.x_bouton_fenetre and mouse[0] <= constantes.x_bouton_fenetre + constantes.LARGEUR_BOUTON) and (mouse[1] >= constantes.y_bouton_fenetre and mouse[1] <= constantes.y_bouton_fenetre + constantes.HAUTEUR_BOUTON):
            return True
        else:
            return False
            
        
        # morceau de code pour tester si ça marche
        # if mouse[0] >= 0 and mouse[1] >= 0:
        #     return True
        # else:
        #     return False
        
def ecran_vierge(fenetre):
    # On commence par effacer l'écran de la frame précédante en coloriant l'écran
    fenetre.fill("white")
                
    # On crée les différentes surfaces
    surface_general = pygame.Surface((constantes.LARGEUR_GENERAL, constantes.HAUTEUR_GENERAL)) # dimensions (largeur-hauteur)
    surface_settings = pygame.Surface((constantes.LARGEUR_SETTINGS, constantes.HAUTEUR_SETTINGS))
    surface_stats = pygame.Surface((constantes.LARGEUR_STATS, constantes.HAUTEUR_STATS))
    
    
    # On leur donne des couleurs
    surface_general.fill("black")  # couleur rouge
    surface_stats.fill((0, 133, 31))  # couleur verte
    surface_settings.fill("blue")  # couleur bleu

    # Button.Afficher(surface_settings)
    image = pygame.transform.scale(pygame.image.load("assets/start_button_troll.png"), (constantes.LARGEUR_BOUTON, constantes.HAUTEUR_BOUTON))
    surface_settings.blit(image, (constantes.x_bouton_settings, constantes.y_bouton_settings))
    
    # On injecte les surfaces sur l'écran
    fenetre.blit(surface_general, (constantes.X_GENERAL, constantes.Y_GENERAL)) # coordonnées (x, y)
    fenetre.blit(surface_settings, (constantes.X_SETTINGS, constantes.Y_SETTINGS))
    fenetre.blit(surface_stats, (constantes.X_STATS, constantes.Y_STATS))
    
    pygame.display.flip()

	
