import calendar as cal
import Database
from datetime import datetime
import Utils

class Motorista():
    def main(idp):
        e = ""
        id_motorista = idp
        while not(e in ["1", "2", "3", "4"]):
            Utils.Util.Separator(False)
            print("Menu principal do motorista")
            print("1 - Criar oferta de carona")
            print("2 - Deletar ofertas")
            print("3 - Ver clientes")
            print("4 - Exportar relatorios")
            print("5 - Exportar graficos")
            print("6 - Sair")
            e = input("Escolha: ")

            Utils.Util.Separator(False)

            if e == "1":
                Motorista.CreateOffer(id_motorista)  
            elif e == "2":
                Motorista.DeleteOffer(id_motorista)
            elif e == "3":
                Motorista.CheckClients(id_motorista)
            elif e == "4":
                Motorista.CreateReport(id_motorista)
                input("Relatorio exportado com sucesso\n")
            elif e == "5":
                Motorista.ExportGraph(id_motorista)
            elif e == "6":
                exit(0)
            else:
                print("Escolha errada, tente novamente")

            Utils.Util.Clear(True)
            e = ""

    def CreateOffer(idp):
        id_motorista = idp
        preco = input("Escreva seu preco: ")
        local = input("Escreva os locais que atende: ")
        now = datetime.now()
        print(f"\nHorario atual: {now}")
        print(cal.month(now.year, now.month))
        
        print("Escolha os dias que pode dar carona separados por virgula")
        dias = input("Dias: ")
        Database.DB.SaveOffer(id_motorista, preco, local, dias, now.month)

        print("Sucesso")

    def CheckClients(idp):
        id_motorista = idp

        t = Database.DB.CheckClients(id_motorista)

        index = ["Usuario: ", "Localidade: ", "Dias: "]
        x = 0
        for client in t:
            x = 0
            Utils.Util.Separator(False)
            for i in client: 
                print(f"{index[x]}{i}")
                x += 1

        Utils.Util.Separator(False)
    
    def ExportGraph(idp):

        t = Database.DB.GetWealth(idp)
        
        x, y, d = [], [], []
        for tup in t:
            x.append(tup[0]) 
            d = tup[1].split(",")
            y.append(float(tup[2]) * len(d))

        Utils.Util.Graph(x, y, "Meses", "Ganhos", "Ganhos mensais")

    def CreateReport(idp):
        
        t = Database.DB.GetWealth(idp)
        
        s = ""
        index = ["Mes: ", "Dias: ", "Ganhos:"]
        for tup in t:
            x = 0
            s += Utils.Util.Separator(True)
            for i in tup:
                s += f"{index[x]}{i}\n"
                x += 1

        with open("relatorio.txt", "w") as f:
            f.write(s)

    def DeleteOffer(idp):
        Database.DB.DeleteOffer(idp)

if __name__ == "__main__":
    Motorista.main()
