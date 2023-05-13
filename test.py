import pygame
import os
os.chdir("natural_selection_sim-main/")
import constantes
import random
pygame.init()
screen = pygame.display.set_mode((constantes.largeur, constantes.hauteur))
clock = pygame.time.Clock()
running = True

max_x = int(constantes.largeur)
max_y = int(constantes.hauteur)
x = random.randint(0, max_x)
y = random.randint(0, max_y)
speed = 15

while running:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de la simulation")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Ferme la fenêtre si tocuhe "echap" pressée
                pygame.quit()
                
    x += random.randint(-speed, speed)
    y += random.randint(-speed, speed)
    
    # Vérifier si l'image est sortie de la surface
    if x < 0:
        x = 0
    elif x > max_x:
        x = max_x
    if y < 0:
        y = 0
    elif y > max_y:
        y = max_y
    
    # Remplir la fenêtre avec la couleur de fond
    screen.fill("white")
    
    # screen.blit(image, (x, y))
    pygame.draw.rect(screen, ("green"), (x, y, 18, 18))
    
    # Mettre à jour l'affichage
    pygame.display.update()
                
    
    

    # image = pygame.transform.scale(pygame.image.load("assets/rubiks.png"), (18, 18))
    
    clock.tick(165)
    
    

    

    

