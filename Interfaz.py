import pygame
import sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Tres en linea')

pantalla = pygame.display.set_mode((500, 400))


blanco = (255, 255, 255)
negro = (0,0,0)
rojo = (255,0,0)

circulo = pygame.image.load('circulo.png')
equis = pygame.image.load('cruz.png')





game_over= False
clock= pygame.time.Clock()
pantalla.fill(rojo)





pygame.draw.rect(pantalla,blanco, (160,42,10,340)) #Horizontal xyxy
pygame.draw.rect(pantalla,blanco, (320,42,10,340)) #Horizontal

pygame.draw.rect(pantalla,blanco, (42,140,400,10)) #Vertical
pygame.draw.rect(pantalla,blanco, (42,280,400,10)) #Vertical

while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.update()


pygame.quit()
def box(x,y):
    cuadrado = pygame.Rect(pantalla,blanco, (x,y,100,100))
    return cuadrado


cuadradoSuperiorIzquierdo = box(20,20)
cuadradoSuperiorDerecho = box()
cuadradoSuperiorCentral = box()

cuadradoCentralIzquierdo = box()
cuadradoCentralCentral = box()
cuadradoCentralDerecho = box()

cuadradoInferiorIzquierdo = box()
cuadradoInferiorCentral = box()
cuadradoInferiorDerecho = box()

pygame.draw.cuadradoSuperiorIzquierdo


def tablero():
    tablero = [(0,0,0), #0.0 0.1 0.2
               (0,0,0), #1.0 1.1 1.2
               (0,0,0)] #2.0 2.1 2.2
    return tablero


    
def turno():
    turno = 0
    while true:
        if turno == 0:
            player1()
        else:
            player2()
        if check_win() == True:
            break

'''
def player1():

def player2():
'''

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

    