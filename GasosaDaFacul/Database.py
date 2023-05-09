import mysql.connector 

conn = mysql.connector.connect(
    user="root",
    password="admin",
    host="localhost",
    database="gasosafacul"
)

class DB:
    @staticmethod
    def Login(user, pas):
        global conn

        sql = f" SELECT COUNT(*) FROM GASOSAFACUL.TBLOGIN L WHERE L.USUARIO = '{user}' AND L.SENHA = '{pas}' "

        c = conn.cursor()
        c.execute(sql)

        r = c.fetchall()

        for row in r:
            i = int(row[0])
        
        return i

    @staticmethod
    def Register(user, pas, tipo):
        global conn

        sql = f" INSERT INTO GASOSAFACUL.TBLOGIN (USUARIO, SENHA, TIPO) VALUES ('{str(user)}', '{str(pas)}', {int(tipo)}) "

        c = conn.cursor()

        c.execute(sql)
        conn.commit()

    @staticmethod
    def GetType(user):
        global conn

        sql = f" SELECT L.TIPO FROM GASOSAFACUL.TBLOGIN L WHERE L.USUARIO = '{user}' "

        c = conn.cursor()

        c.execute(sql)
        r = c.fetchall()

        for row in r:
            t = int(row[0])

        return t

