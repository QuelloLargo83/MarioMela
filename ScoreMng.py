import sqlite3 as sql


class ScoreMng:
    def __init__(self, file):
        self.con  = sql.connect(file)
        self.cur = self.con.cursor()

    def ExecQuery(self, qy):
        res = self.cur.execute(qy)
        self.con.commit()
        return res
    
    def InsertScore(self,score):
        query = "INSERT INTO SCORES (score) values ("+ str(score) +")"
        self.ExecQuery(query)