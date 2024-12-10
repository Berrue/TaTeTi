import pygame
import sys
from pygame.locals import *
import tkinter as tk


pygame.init()
pygame.display.set_caption('Tres en linea')
pantalla = pygame.display.set_mode((500, 400))
blanco = (255, 255, 255)
negro = (0,0,0)
rojo = (255,0,0)
pantalla.fill(rojo)



def box(x, y):
    box = pygame.Rect(x, y, 110, 110)
    pygame.draw.rect(pantalla, negro, box)   
    return box

def tablero():
    tablero = [(0,0,0), #0.0 0.1 0.2
                (0,0,0), #1.0 1.1 1.2
                (0,0,0)] #2.0 2.1 2.2

    lineas = [(160, 42, 10, 340),
                (320, 42, 10, 340),
                (42, 140, 400, 10),
                (42, 280, 400, 10)]
        
    x = [45 , 190, 330]
    y = [30 , 160, 290]
        
    boxes = []       
    for i in range(len(lineas)):
        pygame.draw.rect(pantalla, blanco, lineas[i])

    for i in range(len(x)):
        for j in range(len(y)):
            caja = box(x[i], y[j])
            boxes.append(caja)

    return tablero, boxes



def juego(img, cajas):
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Asegura que el programa salga completamente
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # Obtener la posición del mouse
                for i, caja in enumerate(cajas):
                    if caja.collidepoint(pos):  # Verificar si se hizo clic en una caja
                        # Dibujar la imagen en la caja correspondiente
                        pantalla.blit(img, (caja.x + 5, caja.y + 5))
                        return i  # Retorna el índice de la caja seleccionada

        pygame.display.update()


def player1(cajas):
    equis = pygame.image.load('cruz.png')   
    juego(equis , cajas)

def player2(cajas):
    circulo = pygame.image.load('circulo.png')
    juego(circulo, cajas)

def turno():
    tabla, cajas = tablero()
    turno = 0
    while True:
        if turno > 9:
            print("Empate")
            break
        elif turno % 2 == 0:
            player1(cajas)
            if check_win(tabla,turno) == True:
                break
            turno += 1
        elif turno % 2 == 1: 
            player2(cajas)
            turno += 1
            if check_win(tabla,turno) == True:
                break
        
    
    return True


def check_win(tablero,turno):
    victoria = False
    if tablero[0][0] == tablero[0][1] == tablero[0][2] == 1:
        victoria = True
    elif tablero[1][0] == tablero[1][1] == tablero[1][2] == 1:
        victoria = True
    elif tablero[2][0] == tablero[2][1] == tablero[2][2] == 1:
        victoria = True
    elif tablero[0][0] == tablero[1][0] == tablero[2][0] == 1:
        victoria = True
    elif tablero[0][1] == tablero[1][1] == tablero[2][1] == 1:
        victoria = True
    elif tablero[0][2] == tablero[1][2] == tablero[2][2] == 1:
        victoria = True
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] == 1:
        victoria = True
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] == 1:
        victoria = True

    if victoria == True:
        if turno % 2 == 0:
            print('Gana el jugador 1')
        elif turno % 2 == 1:
            print('Gana el jugador 2')
    return victoria


def game():
    
    
    turno() 
    pygame.display.update()
    
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True


    pygame.quit()

game()