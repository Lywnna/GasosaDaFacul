import mysql.connector 

class DB:
    conn = mysql.connector.connect(
        user="root",
        password="admin",
        host="root",
        database="127.0.0.1"
    )

    @staticmethod
    def Login(user, pas):
        global conn

        sql = f" SELECT COUNT(*) FROM GASOSAFACUL.TBLOGIN L WHERE L.USUARIO = {user} AND L.SENHA = {pas} "
        
        c = conn.cursor()

        c.execute(sql)

        for row in c:
            return row

        return -1



if __name__ == "__main__":
    DB()