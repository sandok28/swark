import pygame, sys, math
from pygame.locals import *

pygame.init()

FPS = 30
frecuencia = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption('Primer Juego en Pygame!')

CIELO = (0,255,255)
NUBE = (255,255,255)
SOL = (255,255,0)
ROJO = (255,0,0)



alucard = pygame.image.load("alucard.png")
luffy = pygame.image.load("luffy.png")
fondo = pygame.image.load("fondo.png")

luffyX = 200
luffyY = 200
aceleradorluffy=0
frenoluffy=0
giroizquierdaluffy=0
giroderechaluffy=0

alucardX = 600
alucardY = 200
aceleradoralucard=0
frenoalucard=0
giroizquierdaalucard=0
giroderechaalucard=0

fondoX = 0
fondoY = 0

NUBE1_DIM = [100,50,200,100]
NUBE2_DIM = [300,100,200,100]

aumX = 0
aumY = 0



fontObject = pygame.font.Font("StripeAttack.ttf",40)
textSurfaceObject = fontObject.render("Primer Juego en PyGame",True,ROJO,CIELO)
textRectObject = textSurfaceObject.get_rect()
textRectObject.center = (200,30)

fontObject2 = pygame.font.Font("StripeAttack.ttf",60)
textSurfaceObject2 = fontObject2.render("Has Ganado el Juego",True,ROJO,CIELO)
textRectObject2 = textSurfaceObject.get_rect()
textRectObject2.center = (400,300)

pygame.mixer.music.load("Molinos_de_viento.mp3")
pygame.mixer.music.play(-1,0.0)

while True: 
    
    
    PANTALLA.blit(fondo,(fondoX,fondoY))
    PANTALLA.blit(alucard,(alucardX,alucardY))
    PANTALLA.blit(luffy,(luffyX,luffyY))
    PANTALLA.blit(textSurfaceObject,textRectObject)
    PANTALLA.blit(textSurfaceObject2,textRectObject)
    
    textSurfaceObject = fontObject.render(str(luffyX),True,ROJO,CIELO)
    textSurfaceObject2 = fontObject2.render(str(alucardX),True,ROJO,CIELO)
    if luffyX >= 800:
        PANTALLA.blit(textSurfaceObject2,textRectObject2)
        
    luffyX=velocidadluffy + sen(anguloluffy)
    luffyY=velocidadluffy + cos(anguloluffy)
    alucardX=velocidadalucard + sen(anguloalucard)
    alucardY=velocidadalucard + cos(anguloalucard)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        pulsada = pygame.key.get_pressed()
     
        if pulsada[K_w]:
            alucardY -= 5
        if pulsada[K_s]:
            alucardY += 5
        if pulsada[K_a]:
            alucardX -= 5
        if pulsada[K_d]:
            alucardX +=5
            
        if pulsada[K_DOWN]:
            luffyY += 5
        if pulsada[K_UP]:
            luffyY -= 5
        if pulsada[K_LEFT]:
            luffyX -= 5
        if pulsada[K_RIGHT]:
            luffyX +=5
                                            
        pygame.display.update()

         
        frecuencia.tick(FPS)




 






