import pygame
import sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Tres en linea')

pantalla = pygame.display.set_mode((500, 400))


blanco = (255, 255, 255)
negro = (0,0,0)
rojo = (255,0,0)

pantalla.fill(rojo)

circulo = pygame.image.load('circulo.png')
equis = pygame.image.load('cruz.png')

clock = pygame.time.Clock()


pygame.draw.rect(pantalla, blanco, (160, 42, 10, 340))  # Línea vertical izquierda
pygame.draw.rect(pantalla, blanco, (320, 42, 10, 340))  # Línea vertical derecha
pygame.draw.rect(pantalla, blanco, (42, 140, 400, 10))  # Línea horizontal superior
pygame.draw.rect(pantalla, blanco, (42, 280, 400, 10))  # Línea horizontal inferior

def box(x, y):
    return pygame.Rect(x, y, 110, 110)

cuadradoSuperiorIzquierdo = box(45,30)
cuadradoSuperiorDerecho = box(190,30)
cuadradoSuperiorCentral = box(330,30)

cuadradoCentralIzquierdo = box(45,160)
cuadradoCentralCentral = box(190,160)
cuadradoCentralDerecho = box(330,160)

cuadradoInferiorIzquierdo = box(45,290)
cuadradoInferiorCentral = box(190,290)
cuadradoInferiorDerecho = box(330,290)


pygame.draw.rect(pantalla, negro, cuadradoSuperiorIzquierdo)  # Rectángulo con borde
pygame.draw.rect(pantalla, negro, cuadradoSuperiorCentral)
pygame.draw.rect(pantalla, negro, cuadradoSuperiorDerecho)

pygame.draw.rect(pantalla, negro, cuadradoCentralIzquierdo)
pygame.draw.rect(pantalla, negro, cuadradoCentralCentral)
pygame.draw.rect(pantalla, negro, cuadradoCentralDerecho)

pygame.draw.rect(pantalla, negro, cuadradoInferiorIzquierdo)
pygame.draw.rect(pantalla, negro, cuadradoInferiorCentral)
pygame.draw.rect(pantalla, negro, cuadradoInferiorDerecho)

def tablero():
    tablero = [(0,0,0), #0.0 0.1 0.2
               (0,0,0), #1.0 1.1 1.2
               (0,0,0)] #2.0 2.1 2.2
    return tablero


'''
def player1():

def player2():
'''   
def turno():
    turno = 0
    while true:
        if turno == 0:
            player1()
        else:
            player2()
        if check_win() == True:
            break



def check_win():
    if tablero[0][0] == tablero[0][1] == tablero[0][2]:
        return True
    elif tablero[1][0] == tablero[1][1] == tablero[1][2]:
        return True
    elif tablero[2][0] == tablero[2][1] == tablero[2][2]:
        return True
    elif tablero[0][0] == tablero[1][0] == tablero[2][0]:
        return True
    elif tablero[0][1] == tablero[1][1] == tablero[2][1]:
        return True
    elif tablero[0][2] == tablero[1][2] == tablero[2][2]:
        return True
    elif tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return True
    elif tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return True

pygame.display.update()
    
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


pygame.quit()