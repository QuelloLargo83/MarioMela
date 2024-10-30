import sqlite3 as sql
from datetime import datetime

import pygame
from pygame._sdl2.video import Window, Renderer, Texture

## GESTORE DATABASE SQLITE PER TOP SCORE

class ScoreMng(Window):
  
    def __init__(self, file, screen):
        super().__init__
        self.con  = sql.connect(file)
        self.cur = self.con.cursor()
        self.screen = screen
        self.showboard = 1

    def ExecSelectQ(self,qy):
        """esegue una query select sul database

        Args:
            qy (_type_): _description_

        Returns:
            : _description_
        """
        res = self.cur.execute(qy)
        resList = res.fetchall()
        return resList

    def ExecQuery(self, qy):
        """esegue una query di tipo alter sul db

        Args:
            qy (str): query

        Returns:
            _type_: 
        """
        res = self.cur.execute(qy)
        self.con.commit()
        return res
    
    def InsertScore(self,score,timer,playerN='player'):
        """inserisce un punteggio nella tabella a database

        Args:
            score (_type_): punteggio
            timer (_type_): tempo massimo della partita
            playerN (str, optional): nome del giocatore. Defaults to 'player'.
        """
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO SCORES (score, date,playerName , timerValue) \
                 VALUES \
                    ("+ str(score) + ","+ \
                    "'" + now +"'," \
                    "'" + playerN + "'," \
                    + str(timer) \
                    + ")"

        
        self.ExecQuery(query)

    def showleader_board(self, font_style, font_color):
        i = 35
        column_space = 400

        head1 = font_style.render(f'DATE', True, font_color)
        head2 = font_style.render(f'PLAYER', True, font_color)
        head3 = font_style.render(f'SCORE', True, font_color)

        dis = self.screen
        dis_width = self.screen.get_width()

        dis.blit(head1, [dis_width / 5, (700 / 4) + 5])
        dis.blit(head2, [dis_width / 5 + column_space, (700 / 4) + 5])
        dis.blit(head3, [dis_width / 5 + column_space + (700 / 4), (700 / 4) + 5])
        
        
        rows = self.ExecSelectQ('SELECT  date, playerName, score  FROM  SCORES ORDER BY score desc LIMIT 10')
        
        
        for row in rows:
            
            column1 = font_style.render('{:<3}'.format(str(row[0])), False, font_color)
            column2 = font_style.render('{:30}'.format(str(row[1])), False, font_color)
            column3 = font_style.render('{:40}'.format(str(row[2])), False, font_color)
            dis.blit(column1, [dis_width / 5, (700 / 4) + i + 5])
            dis.blit(column2, [dis_width / 5 + column_space, (700 / 4) + i + 5])
            dis.blit(column3, [dis_width / 5 + column_space + (700/4), (700 / 4) + i + 5])

            i += 35

        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key ==  pygame.K_SPACE):
                self.showboard = 0


    def aggiorna(self):
        pygame.display.update()