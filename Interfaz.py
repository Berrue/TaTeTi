import pygame, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Tres en linea')

pantalla = pygame.display.set_mode((500, 400))


blanco = (255, 255, 255)
negro = (0,0,0)

circulo = pygame.image.load('circulo.png')
equis = pygame.image.load('cruz.png')

matriz = [[(0,0),(0,0),(0,0)],
          [(0,0),(0,0),(0,0)],
          [(0,0),(0,0),(0,0)]]

game_over= False
clock= pygame.time.Clock()
pantalla.fill(negro)

turno = 0


pygame.draw.rect(pantalla,blanco, (160,42,10,340))

pygame.draw.rect(pantalla,blanco, (320,42,10,340))

pygame.draw.rect(pantalla,blanco, (42,140,400,10))

pygame.draw.rect(pantalla,blanco, (42,280,400,10))

while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.update()


pygame.quit()
