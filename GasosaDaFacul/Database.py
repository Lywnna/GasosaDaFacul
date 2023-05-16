import mysql.connector 
import Utils

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
            Utils.Util.Separator()
            for x in row:
                print(f"{index[i]}{x}")
                i += 1

        Utils.Util.Separator()

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

    @staticmethod
    def CheckActiveContracts(idp):
        global conn

        sql = f"""
            SELECT
            C.ID,
            L.USUARIO,
            M.LOCALIDADE,
            M.PRECO,
            M.DIAS
            FROM gasosafacul.tbcontrato C
            JOIN gasosafacul.tbmotorista M ON M.ID = C.ID_MOTORISTA 
            JOIN gasosafacul.tblogin L ON L.ID = M.ID_PESSOA
            WHERE C.ID_CARONA = {idp}
        """

        c = conn.cursor()
        c.execute(sql)
        r = c.fetchall()

        t = []
        for row in r:
            t.append(row)
        
        return t
    
    @staticmethod
    def GetOfferID(idp):
        global conn

        sql = f"SELECT C.ID FROM gasosafacul.tbcontrato C WHERE C.ID_CARONA = {idp}"
        
        c = conn.cursor()
        c.execute(sql)
        r = c.fetchall()

        t = []
        for row in r:
            for i in row:
                t.append(i)
            
        return t

    @staticmethod
    def DeleteActiveOffer(id):
        global conn

        sql = f"DELETE FROM gasosafacul.tbcontrato C WHERE C.ID = {id}"

        c = conn.cursor()
        c.execute(sql)
        conn.commit()


    @staticmethod
    def CheckClients(id):
        global conn
        
        sql = f"""
            SELECT
            L.USUARIO,
            M.LOCALIDADE,
            M.DIAS
            FROM gasosafacul.tbcontrato C
            JOIN gasosafacul.tbmotorista M ON M.ID = C.ID_MOTORISTA 
            JOIN gasosafacul.tblogin L ON L.ID = C.ID_CARONA
            WHERE M.ID_PESSOA = {id}
        """

        c = conn.cursor()
        c.execute(sql)
        r = c.fetchall()

        t = []
        for row in r:
            t.append(row)

        return t

    @staticmethod
    def GetSpent(idp):
        global conn

        sql = f"""
            SELECT
            M.MES,
            SUM(M.PRECO) AS PRECO
            FROM gasosafacul.tbcontrato C
            JOIN gasosafacul.tbmotorista M ON M.ID = C.ID_MOTORISTA
            WHERE C.ID_CARONA = {idp}
            GROUP BY 1
        """

        c = conn.cursor()
        c.execute(sql)
        r = c.fetchall()

        t = []

        for row in r:
            t.append(row)

        return t

