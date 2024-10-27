import sqlite3 as sql
from datetime import datetime

## GESTORE DATABASE SQLITE PER TOP SCORE

class ScoreMng:
    def __init__(self, file):
        self.con  = sql.connect(file)
        self.cur = self.con.cursor()

    def ExecSelectQ(self,qy):
        """esegue una query select sul database

        Args:
            qy (_type_): _description_

        Returns:
            List: _description_
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