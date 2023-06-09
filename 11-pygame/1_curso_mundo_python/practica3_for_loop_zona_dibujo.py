import pygame
import sys

#Inicializamos Pygame
pygame.init()

#definimos y creamos la ventana del juego
ANCHO = 800
ALTO = 500
screen = pygame.display.set_mode((ANCHO, ALTO))

#Definimos los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)



while(True):
    for evento in pygame.event.get():
        # print(evento)
        if evento.type == pygame.QUIT:# si el usuario toca la cruz de arriba de la ventana ,cierra.
            sys.exit()


    screen.fill(BLANCO) # pintamos la pantalla, en este caso 1ro el fondo.
    #Zona de dibujo ---------
    for x in range(100, 700, 100): #inicia en 100(pixeles donde iniciar), termina en 700(pixeles donde terminar), e incrementa de 100 en 100. 
        pygame.draw.rect(screen, NEGRO, (x, 350, 50, 50))
        pygame.draw.line(screen, AZUL, (x, 0), (x, 100), 5)
    #-----------------------
    pygame.display.flip()# actualiza la pantalla