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
    @staticmethod
    def GetIDPlayer(user):
        global conn
        sql = f" SELECT L.ID FROM GASOSAFACUL.TBLOGIN L WHERE L.USUARIO = '{user}' "

        c = conn.cursor()

        c.execute(sql)

        r = c.fetchall()

        for row in r:
            t = int(row[0])

        return t

    @staticmethod
    def SaveOffer(id_player, preco, localidades, dias):
        global conn

        sql = f" INSERT INTO GASOSAFACUL.TBMOTORISTA (ID_PESSOA, PRECO, LOCALIDADE, DIAS) VALUES ({id_player}, {preco}, '{localidades}', '{dias}')  "

        c = conn.cursor()

        c.execute(sql)
        conn.commit()


    @staticmethod
    def SeeOffers():
        global conn 
        sql = """
            SELECT
            M.ID,
            L.USUARIO,
            M.PRECO,
            M.LOCALIDADE,
            M.DIAS
            FROM gasosafacul.tbmotorista M
            JOIN gasosafacul.tblogin L ON L.ID = M.ID_PESSOA
        """
        c = conn.cursor()

        c.execute(sql)
        r = c.fetchall()

        index = ["Identificador: ","Motorista: ", "Preco: ", "Localidade: ", "Dias: "]
        for row in r:
            i = 0
            print("=-=" * 20)
            for x in row:
                print(f"{index[i]}{x}")
                i += 1
        print("=-=" * 20)

        sql = "SELECT M.ID FROM gasosafacul.tbmotorista M"
        
        c = conn.cursor()

        c.execute(sql)
        r = c.fetchall()

        t = []
        for row in r:
            for i in row:
                t.append(i)

        return t

    @staticmethod
    def SaveContract(id_carona, id_motorista):
        global conn

        sql = f"INSERT INTO GASOSAFACUL.TBCONTRATO (ID_MOTORISTA, ID_CARONA) VALUES ({id_motorista}, {id_carona})"
        
        c = conn.cursor()
        c.execute(sql)
        conn.commit()




                
