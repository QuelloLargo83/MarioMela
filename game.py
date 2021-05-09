#!/usr/bin/python3

import pygame
import random

pygame.init()

FPS = 50
TIMER_meleSet = 1000 # millisecondi
sfondo = pygame.image.load('IMMAGINI/background.png')
mario = pygame.image.load('IMMAGINI/mario.png')
mela_dis = pygame.image.load('IMMAGINI/mela.png')
gameover = pygame.image.load('IMMAGINI/gameover.png')
gameover = pygame.transform.scale2x(gameover) # raddoppio le dimensioni di gameover
width = sfondo.get_width()
height = sfondo.get_height()
screensize = (width,height)
screen = pygame.display.set_mode(screensize)

#timer
TIMER_mele = pygame.USEREVENT
pygame.time.set_timer(TIMER_mele,TIMER_meleSet) #il secondo parametro indica ogni quanto viene triggerato il timer

#coordinate iniziali di Mario
mariox = 100
marioy = 910

mario_rect = mario.get_rect(center = (mariox,marioy)) #creo un rettangolo intorno a mario


class mela_c():
    def __init__(self):
        self.x = random.randint(0,width) # dimensione random da 0 fino alla larghezza massima dello schermo di gioco
        self.y = random.randint(0,height) # dimensione random da 0 fino all altezza massima dello schermo i gioco
        self.rect = mela_dis.get_rect(center = (self.x,self.y)) # creo un rettangolo intorno all'oggetto
    def disegna(self,self_rect):
        screen.blit(mela_dis,self.rect)
    def check_collision(self,self_rect): #controllo la collisione tra mario e le mele
        self.attrib = ''
        if mario_rect.colliderect(self.rect):
            self.attrib = (str(self.__getattribute__)) # ricavo un id della mela che ha generato la collisione
            # for index in enumerate(mele):
            #     print(index)  #anche qui ho un id dell'oggetto
            #stop()
            mangia_mela()
        
          
# gameover
def stop():
    pausa = True
    #avviso che si puo ricominciare
    black=(0,0,0) #colore scritta
    myFont = pygame.font.SysFont("Consolas", 14)
    Label = myFont.render("PREMI SPAZIO PER RICOMINCIARE", 1, black)
    screen.blit(Label, (width/2-60,height/2+100))
    screen.blit(gameover,(width/2 - 130,height/2)) #disegno gameover
    aggiorna()

    while pausa:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
              del mele[0:-1] #cancello tutte le mele
              mario_rect.centerx = 100
              mario_rect.centery = 910
              pausa = False
            if event.type == pygame.QUIT: # do comunque la possibilita di uscire
              pygame.quit() 

# cancella la mela che ha generato la collisione
def mangia_mela():
    for i in range(len(mele)):
      if mele[i].attrib != '': #ho inizializzato vuoto quindi quando viene assegnato qualcosa è l'id della mela che ha generata la collisione
        idx_mela_collisione = i #appoggio id della mela che ha generato collisione
    del mele[idx_mela_collisione] #cancello solo la mela che ha generato la collisione  

    # rallento la produzione delle mele
    global TIMER_meleSet
    #print(TIMER_meleSet)
    TIMER_meleSet = TIMER_meleSet + 1000
    pygame.time.set_timer(TIMER_mele,TIMER_meleSet)

def inizializza():
    global mele
    mele = []
    mele.append(mela_c()) #inizio a popolare la la lista di istanze della classe mele_c
    
def disegna():
    screen.blit(sfondo,(0,0))
    screen.blit(mario,mario_rect) 
    for m in mele:
        m.disegna(m.rect)

def collisione():
    for m in mele:
        m.check_collision(m.rect)

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS) #regola la velocità del ciclo principale

inizializza()

#gameloop
while 1:
    #mario_rect.centerx += 1 #muovo mario in avanti di un pixel
    for event in pygame.event.get():
        # chiudo la finestra, chiudo il gioco
        if event.type == pygame.QUIT:
           pygame.quit()     
        
        # aggiungo le mele a tempo
        if event.type == TIMER_mele:
            mele.append(mela_c())

        # muovo mario con le frecce
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            mario_rect.centerx += 20
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            mario_rect.centerx -= 20  
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            mario_rect.centery -= 20
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            mario_rect.centery += 20

    #se mario esce dallo schermo di gioco, riposizionalo all'inizio   
    if mario_rect.right >= width or mario_rect.bottom >= height or mario_rect.left <= 0 or mario_rect.top <=0: 
            mario_rect.centerx = 100
            mario_rect.centery = 910

    disegna()
    aggiorna()
    collisione() 
    
    