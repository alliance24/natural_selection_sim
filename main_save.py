import pygame
# from simulation import Simulation
from creature import Creature

pygame.init()

# On récupère les dimensions de l'écran
infos = pygame.display.Info()
largeur = infos.current_w
hauteur = infos.current_h

# On génère la fenêtre
pygame.display.set_caption("Simulation de la vie")
screen = pygame.display.set_mode((largeur, hauteur))

creature = Creature()

running = True

# Maintiens la fenêtre tant que running = True
while running:
    
    # Remplir la fenêtre avec la couleur de fond
    screen.fill("white")
    
    # ----- SURFACES -----
    # Surface géneral
    surface_general = pygame.Surface((0.98*hauteur, 0.98*hauteur)) # dimensions
    surface_general.fill((255, 0, 0))  # couleur rouge
    # screen.blit(surface_general, (0.01*hauteur, 0.01*hauteur)) # position
    
    # Surface stats 
    surface_stats = pygame.Surface((largeur-hauteur*1.01, 0.48*hauteur))
    surface_stats.fill((0, 255, 0))  # couleur verte
    screen.blit(surface_stats, (hauteur, 0.01*hauteur))
    
    # Surface stats 
    surface_settings = pygame.Surface((largeur-hauteur*1.01, 0.48*hauteur))
    surface_settings.fill((0, 0, 255))  # couleur bleu
    screen.blit(surface_settings, (hauteur, 0.51*hauteur))
    
    # Creature
    # Injection de la creature sur la surface général
    surface_general.blit(creature.image, creature.rect)
    
    # Injection de la surface général sur le screen
    screen.blit(surface_general, (0.01*hauteur, 0.01*hauteur))
    
    # Mise à jour de l'écran
    pygame.display.flip()
    
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de la simulation")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                

    
    
    
