import Database


class Carona():
    def main(idp):
        id_player = idp
        e = ""
        while not(e in ["1", "2", "3", "4", "5"]):
            print("=-=" * 20)
            print("Menu principal")
            print("1 - Ver ofertas de carona")
            print("2 - Ver ofertas ativas")
            print("3 - Exportar relatorios")
            print("4 - Exportar graficos")
            print("5 - Sair")
            e = input("Escolha: ")
            
            if e == "1":
                Carona.ChooseOffers(id_player)
            elif e == "2":
                Carona.CheckOffer(id_player)
            elif e == "3":
                print()
            elif e == "4":
                print()
            
            print("\n")
            e = ""

    def ChooseOffers(id_player):
        print("\n")
        print("Ofertas")
        IDs = Database.DB.SeeOffers()
        x = ""
        i = 0
        while not(x in IDs):
            if i > 0:
                print("Escolha invalida, tente novamente")
            try:
                x = int(input("\n\nUse o numero identificador para escolher\nEscolha uma das ofertas: "))
            except:
                print("Algo alem de numero foi escrito, tente novamente")
            i += 1
        
        Database.DB.SaveContract(id_player, x)

        print("Parabens voce contratou o sevico")

    def CheckOffer(id_player):
        print("Oferta ativa")
        offers = Database.DB.CheckActiveContracts(id_player)

        index = ["ID: ", "Usuario: ", "Localidade: ", "Preco: ", "Dias: "]
        for tup in offers:
            i = 0
            print("=-=" * 20)
            for ele in tup:
                print(f"{index[i]}{ele}")
                i += 1

        input("pause")













if __name__ == "__main__":
    Carona.main()
