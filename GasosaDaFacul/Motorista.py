import calendar as cal
from datetime import datetime
import Database

class Motorista():
    def main(idp):
        e = ""
        id_player = idp
        while not(e in ["1", "2", "3", "4", "5"]):
            print("=-=" * 20)
            print("Menu principal")
            print("1 - Criar oferta de carona")
            print("2 - Ver clientes")
            print("3 - Exportar relatorios")
            print("4 - Exportar graficos")
            print("5 - Sair")
            e = input("Escolha: ")

            if e == "1":
                Motorista.CreateOffer(id_player)  
                print("Sucesso!")

            elif e == "2":
                print()
            elif e == "3":
                print()
            elif e == "4":
                print()

            e = ""

    def CreateOffer(idp):
        id_player = idp

        print("\n")
        print("=-="*20)
        preco = input("Escreva seu preco: ")
        local = input("Escreva os locais que atende: ")
        now = datetime.now()
        print(f"\nHorario atual: {now}")
        print(cal.month(now.year, now.month))
        
        print("Escolha os dias que pode dar carona separados por virgula")
        dias = input("Dias: ")
        Database.DB.SaveOffer(id_player, preco, local, dias)
                




if __name__ == "__main__":
    Motorista.main()
