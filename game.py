#!/usr/bin/python3

import pygame
# import random
import math
import os
from OptionChooser import *
from ScoreMng import *
from cfg import *
from Bowser import *



# settaggio percorso e file database
cwd = os.path.dirname(__file__)
dbfile = cwd +  bars + DB_PATH_NAME + bars + SCORE_DB_FILE

pygame.init()


pygame.display.set_caption("MARIO MELA") #titolo finestra


sfondo = pygame.image.load(BG_IMAGE)
width = sfondo.get_width()
height = sfondo.get_height()
screensize = (width,height)
screen = pygame.display.set_mode(screensize)
counter_gioco = MAX_TIME    # secondi di gioco
marioXinit = MARIO_X_INIT            # posizione X iniziale di mario all'interno della finestra
marioYinit = MARIO_Y_INIT            # posizione Y iniziale di mario all'interno della finestra
mario_speed = MARIO_SPEED
mario_angle = MARIO_ANGLE
mela_dis = pygame.image.load(MELA_IMG)
gameover = pygame.image.load(GAME_OVER_IMG)
gameover = pygame.transform.scale2x(gameover) # raddoppio le dimensioni di gameover
mela_sound = pygame.mixer.Sound(MELA_HIT_SOUND)     
mariojump_sound = pygame.mixer.Sound(MARIO_JUMP_SOUND)
Punteggio = 0

# Init oggetto Salvataggio Punteggio
ScMng = ScoreMng(dbfile, screen) 

def SchermataIniziale():
    """Gestione Schermata iniziale

    Returns:
        pygame.image : immagine pygame del personaggio da usare
    """
    ### SCHERMATA INIZIALE ####
    winOption = OptionChooser(
                            screen, 
                            bg=BG_IMAGE,
                            choiceimg=CHOICE_IMAGE,
                            p1image=P1_IMAGE,
                            p2image=P2_IMAGE,
                            font=FONTNAME,
                            fontcolor=FONTCOLOR
                            )

    while winOption.running == 1:
        winOption.disegnaschermo()
        winOption.aggiorna()

    match int(winOption.ret_scelta):
        case 1:
            mario = pygame.image.load(P1_IMAGE)
        case 2:
            mario = pygame.image.load(P2_IMAGE)
    
    return mario
    ###############################

def MarioInit(mario):
    """Inizializza il personaggio

    Args:
        mario (pygame.image): immagine pygame del personaggio

    Returns:
        _type_: rettangolo del personaggio, rect pers flippato
    """
    mario_flip = pygame.transform.flip(mario,True,False) # Mario girato a sx

    #coordinate iniziali di Mario
    mariox = marioXinit
    marioy = marioYinit

    mario_rect = mario.get_rect(center = (mariox,marioy)) #creo un rettangolo intorno a mario

    return mario_rect,mario_flip

#timer frequenza mele
TIMER_mele = pygame.USEREVENT
pygame.time.set_timer(TIMER_mele,TIMER_meleSet) #il secondo parametro indica ogni quanto viene triggerato il timer

#timer di gioco
Timer_gioco = pygame.USEREVENT +1 
pygame.time.set_timer(Timer_gioco,TIMER_giocoSet)
class mela_c():
    def __init__(self):
        self.x = random.randint(0,width)                        # dimensione random da 0 fino alla larghezza massima dello schermo di gioco
        self.y = random.randint(0,height)                       # dimensione random da 0 fino all altezza massima dello schermo i gioco
        self.rect = mela_dis.get_rect(center = (self.x,self.y)) # creo un rettangolo intorno all'oggetto
        self.attrib = ''
    def disegna(self,self_rect):
        """disegna la mela con il suo rettangolo
        """
        screen.blit(mela_dis,self.rect)
    def check_collision(self,self_rect): 
        """controllo la collisione tra mario e le mele
        """
        #self.attrib = ''
        if mario_rect.colliderect(self.rect):
            self.attrib = (str(self.__getattribute__))          # ricavo un id della mela che ha generato la collisione
            mangia_mela()

# coordinate iniziali di bowser
bowserXinit = width/2
bowserYinit = height/2 +100
# creo bowser
bowserobj = Bowser(BOWSER_IMG, bowserXinit, bowserYinit)


############      
# GAMEOVER #
############
def stop():
    """Definisce cosa avviene in caso di gameover
    """
    pygame.mixer.music.load(GAME_OVER_SOUND)
    pygame.mixer.music.play(0)
    pausa = True

    #avviso che si puo ricominciare
    myFont = pygame.font.SysFont(FONTNAME, 14)
    Label = myFont.render("PREMI SPAZIO PER RICOMINCIARE", 1, FONTCOLOR)
    screen.blit(Label, (width/2-60,height/2+100))
    screen.blit(gameover,(width/2 - 130,height/2)) #disegno gameover
    aggiorna()

    while pausa:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
              del mele[0:-1]                #cancello tutte le mele
            
              InitMusic()
              mario_rect.centerx = marioXinit
              mario_rect.centery = marioYinit
              global Punteggio
              
              # inserisco il punteggio attuale nel database
              ScMng.InsertScore(score=Punteggio,timer=MAX_TIME)
              
              # mostro i top scorer
              fontScore = pygame.font.SysFont(FONTNAME, 16)
              ScMng.showboard = 1
              while ScMng.showboard == 1:
                ScMng.showleader_board(fontScore, FONTCOLOR)
                ScMng.aggiorna()
                

              Punteggio = 0
              pausa = False
              
              

            if event.type == pygame.QUIT:   # do comunque la possibilita di uscire
              pygame.quit() 
    

def pausa():
    """gestione pausa gioco
    """
    pausa = True
    pygame.mixer.music.pause()

    #avviso che si puo ricominciare
    myFont = pygame.font.SysFont(FONTNAME, 14)
    Label = myFont.render("PREMI SPAZIO PER RICOMINCIARE", 1, FONTCOLOR)
    screen.blit(Label, (width/2-60,height/2+100))
    aggiorna()

    while pausa:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                pygame.mixer.music.unpause()
                pausa = False

# cancella la mela che ha generato la collisione
def mangia_mela():
    """gestione evento collisione tra Mario e la mela
    """
    for i in range(len(mele)):
      if mele[i].attrib != '':      # ho inizializzato vuoto quindi quando viene assegnato qualcosa è l'id della mela che ha generata la collisione
        idx_mela_collisione = i     # appoggio id della mela che ha generato collisione
    del mele[idx_mela_collisione]   # cancello solo la mela che ha generato la collisione  
    global Punteggio
    Punteggio += 1                  # ad ogni mela aumento il punteggio
    mela_sound.play()               #suono

    # rallento la produzione delle mele
    # global TIMER_meleSet
    # TIMER_meleSet = TIMER_meleSet + 1000
    # pygame.time.set_timer(TIMER_mele,TIMER_meleSet)

def InitMusic():
    """Inizializzazione musica di sistema
    """
    pygame.mixer.pre_init(22050, 16, 2, 8192)
    pygame.mixer.music.load(MAIN_THEME)
    pygame.mixer.music.play(-1)

def inizializza():
    """gestisce inizializzazione del gioco
    """
    global mele
    mele = []
    mele.append(mela_c())           #inizio a popolare la la lista di istanze della classe mele_c
    
    InitMusic()
    mario = SchermataIniziale()
    mario_rect, mario_flip = MarioInit(mario)

    return mario_rect, mario, mario_flip
    
def disegna():
    """gestisce il disegno dinamico dello sfondo e degli oggetti
    """
    global left
    screen.blit(sfondo,(0,0))
    if left == False:
        screen.blit(mario,mario_rect) 
    if left == True:
        screen.blit(mario_flip,mario_rect)
    for m in mele:
        m.disegna(m.rect)

    #disegno il punteggio
    # black=(0,0,0) #scritta nera
    myFont = pygame.font.SysFont(FONTNAME, 36)
    Label_Punteggio = myFont.render('SCORE: ' + str(Punteggio), 1, FONTCOLOR)
    screen.blit(Label_Punteggio, (10, 10))   

    #disegno tempo di gioco
    Label_CounterGioco = myFont.render('TIME: ' + str(counter_gioco), 1, FONTCOLOR)
    screen.blit(Label_CounterGioco, (10, 40))   
    
    # disegno il nemico
    bowserobj.disegna(screen)

def collisione():
    """gestione collisione tra i vari oggetti dello schermo
    """
    for m in mele:
        m.check_collision(m.rect)

def aggiorna():
    """gestione aggiornamento schermo
    """
    pygame.display.update()
    pygame.time.Clock().tick(FPS) #regola la velocità del ciclo principale


# inizializzo il personaggio
mario_rect, mario, mario_flip = inizializza()


##############
## GAMELOOP ##
##############
while 1:
    

    mario_rect.centery += VEL_grav #gravita
    
    # EVENTI GESTITI DURANTE IL GIOCO #
    for event in pygame.event.get():
        # chiudo la finestra, chiudo il gioco
        # if event.type == pygame.QUIT:
        #    pygame.quit()     
        
        if (event.type == pygame.KEYDOWN and event.key ==  pygame.K_ESCAPE):
                pygame.quit()
        
        # aggiungo le mele a tempo
        if event.type == TIMER_mele:
            mele.append(mela_c())

        if event.type == Timer_gioco:
            #global counter_gioco
            counter_gioco -= 1    


        # muovo mario con le frecce
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            mario_rect.centerx += 20
            left = False
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            mario_rect.centerx -= 20 
            left = True
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            mariojump_sound.play()
            mario_rect.centery -= 80
            
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            mario_rect.centery += 20

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pausa()
    
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
        mario_rect, mario, mario_flip = inizializza() # ad ogni game over rifaccio scegliere il personaggio
    
    # gestione movimento casuale di bowser
    if (pygame.time.get_ticks() % 2):
        direzione = random.randint(1,4)
        bowserobj.random_move(direzione)

    # limito i movimenti di bowser
    bowserobj.movement_limits(width)

    disegna()
    aggiorna()
    collisione() # controllo collisione con le mele
    bowser_collision = bowserobj.check_collision(mario_rect) # controllo collisione con bowser
    

    # se il personaggio colpisce il cattivo
    if bowser_collision:
        bowserobj.collision = 0
        counter_gioco = MAX_TIME
        stop()        
        mario_rect, mario, mario_flip = inizializza() # ad ogni game over rifaccio scegliere il personaggio