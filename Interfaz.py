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
violeta = (137,71,200)
pantalla.fill(negro)



def box(x, y):
    box = pygame.Rect(x, y, 110, 110)
    pygame.draw.rect(pantalla, negro, box)   
    return box

def tablero():
    tablero = [[0,0,0], #0.0 0.1 0.2
                [0,0,0], #1.0 1.1 1.2
                [0,0,0]] #2.0 2.1 2.2

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



def juego(img, cajas, tablero):
    

    print (tablero)
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Asegura que el programa salga completamente
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # Obtener la posición del mouse
            
                for i, caja in enumerate(cajas):
                    if caja.collidepoint(pos):  # Verificar si se hizo clic en una caja# Dibujar la imagen en la caja correspondiente
                        fila = i // 3  # División entera para obtener la fila (0, 1, 2)
                        columna = i % 3  # Módulo para obtener la columna (0, 1, 2)
                        if tablero[fila][columna] == 0:
                            pantalla.blit(img, (caja.x + 5, caja.y + 5))
                            corriendo = False
                        else:
                            print("clickea un valido boludo")
                        
                        
                        
                        
    
 
        pygame.display.update()
    return tablero, fila, columna


def player1(cajas, tabla):
    equis = pygame.transform.scale(pygame.image.load('cruz.png'),(80,80))   
    tabla, fila, columna = juego(equis , cajas, tabla)
    tabla[fila][columna] = 1
    return tabla
def player2(cajas, tabla):
    circulo = pygame.transform.scale(pygame.image.load('circulo.png'),(80,80))
    tabla, fila, columna = juego(circulo, cajas, tabla)
    tabla[fila][columna] = 2
    return tabla


def turno():
    tabla, cajas = tablero()
    turno = 0
    while True:
        if turno > 9:
            print("Empate")
            break
        elif turno % 2 == 0:
            tabla = player1(cajas, tabla)
            if check_win(tabla,turno) == True:
               break
            turno += 1
        elif turno % 2 == 1: 
            tabla = player2(cajas, tabla)
            turno += 1
            if check_win(tabla,turno) == True:
               break
        
    
    return True


def check_win(tablero,turno):
    victoria = False
    if tablero[0][0] == tablero[0][1] == tablero[0][2] == 1 or tablero[0][0] == tablero[0][1] == tablero[0][2] == 2:
        victoria = True
        pygame.draw.rect(pantalla, violeta, (90, 30, 10, 350))
    elif tablero[1][0] == tablero[1][1] == tablero[1][2] == 1 or tablero[1][0] == tablero[1][1] == tablero[1][2] == 2:
        victoria = True
        pygame.draw.rect(pantalla, violeta, (240, 30, 10, 350))
    elif tablero[2][0] == tablero[2][1] == tablero[2][2] == 1 or tablero[2][0] == tablero[2][1] == tablero[2][2] == 2:
        victoria = True
        pygame.draw.rect(pantalla, violeta, (370, 30, 10, 350))
    elif tablero[0][0] == tablero[1][0] == tablero[2][0] == 1 or tablero[0][0] == tablero[1][0] == tablero[2][0] == 2:
        victoria = True
        pygame.draw.rect(pantalla, violeta, (42, 75, 400, 10))
    elif tablero[0][1] == tablero[1][1] == tablero[2][1] == 1 or tablero[0][1] == tablero[1][1] == tablero[2][1] == 2:
        victoria = True
        pygame.draw.rect(pantalla, violeta, (42, 210, 400, 10))
    elif tablero[0][2] == tablero[1][2] == tablero[2][2] == 1 or tablero[0][2] == tablero[1][2] == tablero[2][2] == 2:
        victoria = True
        pygame.draw.rect(pantalla, violeta, (42, 335, 400, 10))
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] == 1 or tablero[0][0] == tablero[1][1] == tablero[2][2] == 2:
        victoria = True
        pygame.draw.line(pantalla, violeta, (40, 25), (400, 380), 10)
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] == 1 or tablero[0][2] == tablero[1][1] == tablero[2][0] == 2:
        victoria = True
        pygame.draw.line(pantalla, violeta, (410,40),(60,360), 10)
    if victoria == True:
        if turno % 2 == 0:
            print('Gana el jugador 1')
        elif turno % 2 == 1:
            print('Gana el jugador 2')
    return victoria

def game():
    while True:  # Bucle para reiniciar el juego
        pantalla.fill(negro)  # Limpia la pantalla
        tabla, cajas = tablero()  # Reinicia el tablero
        turno_actual = 0
        partida_terminada = False

        while not partida_terminada:
            if turno_actual >= 9:
                print("Empate")
                partida_terminada = True
            elif turno_actual % 2 == 0:
                tabla = player1(cajas, tabla)
                if check_win(tabla, turno_actual):
                    partida_terminada = True
                turno_actual += 1
            elif turno_actual % 2 == 1:
                tabla = player2(cajas, tabla)
                if check_win(tabla, turno_actual):
                    partida_terminada = True
                turno_actual += 1

            pygame.display.update()

        pygame.time.wait(3000)

        print("Reiniciando el juego...")

game()