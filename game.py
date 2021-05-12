#!/usr/bin/python3

import pygame
import random

pygame.init()

pygame.display.set_caption("MARIO MELA") #titolo finestra
FPS = 50
TIMER_meleSet = 1000 # millisecondi
TIMER_giocoSet = 1000 #timeout di gioco
MAX_TIME = 60
counter_gioco = MAX_TIME #secondi di gioco
marioXinit = 100
marioYinit = 973
left = False
VEL_grav = 2

sfondo = pygame.image.load('IMMAGINI/background.png')
mario = pygame.image.load('IMMAGINI/mario.png')
mario_flip = pygame.transform.flip(mario,True,False) # Mario girato a sx
mela_dis = pygame.image.load('IMMAGINI/mela.png')
gameover = pygame.image.load('IMMAGINI/gameover.png')
gameover = pygame.transform.scale2x(gameover) # raddoppio le dimensioni di gameover
width = sfondo.get_width()
height = sfondo.get_height()
screensize = (width,height)
screen = pygame.display.set_mode(screensize)
Punteggio = 0

#timer frequenza mele
TIMER_mele = pygame.USEREVENT
pygame.time.set_timer(TIMER_mele,TIMER_meleSet) #il secondo parametro indica ogni quanto viene triggerato il timer

#timer di gioco
Timer_gioco = pygame.USEREVENT +1 
pygame.time.set_timer(Timer_gioco,TIMER_giocoSet)

#coordinate iniziali di Mario
mariox = marioXinit
marioy = marioYinit

mario_rect = mario.get_rect(center = (mariox,marioy)) #creo un rettangolo intorno a mario


class mela_c():
    def __init__(self):
        self.x = random.randint(0,width) # dimensione random da 0 fino alla larghezza massima dello schermo di gioco
        self.y = random.randint(0,height) # dimensione random da 0 fino all altezza massima dello schermo i gioco
        self.rect = mela_dis.get_rect(center = (self.x,self.y)) # creo un rettangolo intorno all'oggetto
        self.attrib = ''
    def disegna(self,self_rect):
        screen.blit(mela_dis,self.rect)
    def check_collision(self,self_rect): #controllo la collisione tra mario e le mele
        #self.attrib = ''
        if mario_rect.colliderect(self.rect):
            self.attrib = (str(self.__getattribute__)) # ricavo un id della mela che ha generato la collisione
            mangia_mela()
        
          
# gameover
def stop():
    pygame.mixer.music.load('MUSIC/smb_gameover.wav')
    pygame.mixer.music.play(0)
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
              mario_rect.centerx = marioXinit
              mario_rect.centery = marioYinit
              global Punteggio
              Punteggio = 0
              pausa = False
            if event.type == pygame.QUIT: # do comunque la possibilita di uscire
              pygame.quit() 

# cancella la mela che ha generato la collisione
def mangia_mela():
    for i in range(len(mele)):
      if mele[i].attrib != '': #ho inizializzato vuoto quindi quando viene assegnato qualcosa è l'id della mela che ha generata la collisione
        idx_mela_collisione = i #appoggio id della mela che ha generato collisione
    del mele[idx_mela_collisione] #cancello solo la mela che ha generato la collisione  
    global Punteggio
    Punteggio += 1 # ad ogni mela aumento il punteggio
    pygame.mixer.music.load('SFX/smb_coin.wav')
    pygame.mixer.music.play(0)

    # rallento la produzione delle mele
    # global TIMER_meleSet
    # TIMER_meleSet = TIMER_meleSet + 1000
    # pygame.time.set_timer(TIMER_mele,TIMER_meleSet)

def inizializza():
    global mele
    mele = []
    mele.append(mela_c()) #inizio a popolare la la lista di istanze della classe mele_c
    
def disegna():
    global left
    screen.blit(sfondo,(0,0))
    if left == False:
        screen.blit(mario,mario_rect) 
    if left == True:
        screen.blit(mario_flip,mario_rect)
    for m in mele:
        m.disegna(m.rect)

    #disegno il punteggio
    black=(0,0,0) #scritta nera
    myFont = pygame.font.SysFont("Consolas", 36)
    Label_Punteggio = myFont.render('SCORE: ' + str(Punteggio), 1, black)
    screen.blit(Label_Punteggio, (10, 10))   

    #disegno tempo di gioco
    Label_CounterGioco = myFont.render('TIME: ' + str(counter_gioco), 1, black)
    screen.blit(Label_CounterGioco, (10, 40))   


def collisione():
    for m in mele:
        m.check_collision(m.rect)

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS) #regola la velocità del ciclo principale

inizializza()

##############
## GAMELOOP ##
##############
while 1:
    mario_rect.centery += VEL_grav #gravita
    for event in pygame.event.get():
        # chiudo la finestra, chiudo il gioco
        if event.type == pygame.QUIT:
           pygame.quit()     
        
        # aggiungo le mele a tempo
        if event.type == TIMER_mele:
            mele.append(mela_c())

        if event.type == Timer_gioco:
            #global counter_gioco
            counter_gioco -= 1    


        # muovo mario con le frecce e salta con spazio
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            mario_rect.centerx += 20
            left = False
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            mario_rect.centerx -= 20 
            left = True
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            mario_rect.centery -= 80
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            mario_rect.centery += 20

    #############################
    ## LIMITI MOVIMENTI MARIO ###
    #############################
    #scorrimento infinito a sx
    if mario_rect.right <= 0: 
            mario_rect.right = width-1
    # scorrimento a dx infinito
    if mario_rect.right >= width:
            mario_rect.left = 1
    #mario non puo andare sotto il pavimento
    if mario_rect.bottom >= marioYinit + mario_rect.height/2 +1:
            mario_rect.centery = marioYinit 
    #mario non puo uscire da sopra        
    if mario_rect.top <=0:
            mario_rect.top = 0

    #se scade tempo di gioco
    if  counter_gioco ==0:
        counter_gioco = MAX_TIME
        stop()        

    disegna()
    aggiorna()
    collisione() 



    
    