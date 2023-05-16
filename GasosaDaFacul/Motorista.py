import calendar as cal
from datetime import datetime
import Database
import Utils

class Motorista():
    def main(idp):
        e = ""
        id_motorista = idp
        while not(e in ["1", "2", "3", "4"]):
            Utils.Util.Separator()
            print("Menu principal do motorista")
            print("1 - Criar oferta de carona")
            print("2 - Ver clientes")
            print("3 - Exportar relatorios")
            print("4 - Exportar graficos")
            print("5 - Sair")
            e = input("Escolha: ")

            Utils.Util.Separator()

            if e == "1":
                Motorista.CreateOffer(id_motorista)  
            elif e == "2":
                Motorista.CheckClients(id_motorista)
            elif e == "3":
                print()
            elif e == "4":
                print()
            else:
                exit(0)

            Utils.Util.Clear()
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
        Database.DB.SaveOffer(id_motorista, preco, local, dias)

        print("Sucesso")

    def CheckClients(idp):
        id_motorista = idp

        t = Database.DB.CheckClients(id_motorista)

        index = ["Usuario: ", "Localidade: ", "Dias: "]
        x = 0
        for client in t:
            x += 0
            Utils.Util.Separator()
            for i in client: 
                print(f"{index[x]}{i}")
                x += 1

        Utils.Util.Separator()
                




if __name__ == "__main__":
    Motorista.main()
