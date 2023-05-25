import pygame
from pygame_textinput import TextInput

pygame.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définir la taille de la fenêtre
largeur = 800
hauteur = 600
taille_fenetre = (largeur, hauteur)

# Initialiser la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Entrée de texte")

# Créer une instance de TextInput
text_input = TextInput()

# Boucle principale du jeu
terminer = False
clock = pygame.time.Clock()

while not terminer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminer = True

        # Passer les événements à l'instance de TextInput
        text_input.update(event)

    # Effacer l'écran
    fenetre.fill(BLANC)

    # Obtenir le texte entré
    texte = text_input.get_text()

    # Afficher le texte dans le bloc
    police = pygame.font.Font(None, 32)
    bloc_texte = police.render(texte, True, NOIR)
    fenetre.blit(bloc_texte, (200, 200))

    # Afficher le bloc de saisie de texte
    surface_text_input = text_input.get_surface()
    fenetre.blit(surface_text_input, (200, 250))

    pygame.display.flip()
    clock.tick(60)

# Quitter Pygame
pygame.quit()
