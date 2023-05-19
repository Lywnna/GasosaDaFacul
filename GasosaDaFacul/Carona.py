import Database
import Utils


class Carona():
    def main(idp):
        id_player = idp
        e = ""
        while not(e in ["1", "2", "3", "4"]):
            Utils.Util.Separator(False)
            print("Menu principal do carona")
            print("1 - Ver ofertas de carona")
            print("2 - Ver ofertas ativas")
            print("3 - Exportar relatorios")
            print("4 - Exportar graficos")
            print("5 - Sair")
            e = input("Escolha: ")
            
            Utils.Util.Separator(False)

            if e == "1":
                Carona.ChooseOffers(id_player)
            elif e == "2":
                Carona.CheckOffer(id_player)
            elif e == "3":
                Carona.ExportReport(id_player)
                input("Relatorio foi exportado com sucesso\n")
            elif e == "4":
                Carona.ExportGraph(id_player)
            else:
                exit(0)
            
            Utils.Util.Clear()
            e = ""

    def ChooseOffers(id_player):
        print("Ofertas")
        IDs = Database.DB.SeeOffers()
        x = ""
        i = 0
        while not(x in IDs):
            if i > 0:
                print("Escolha invalida, tente novamente")
            try:
                x = input("\n\nUse o numero identificador para escolher, ou digite 0 para sair\nEscolha uma das ofertas: ")
                if x == "0":
                    print("\n")
                    return
                x = int(x)
            except:
                print("Algo alem de numero foi escrito, tente novamente")
            i += 1
        
        Database.DB.SaveContract(id_player, x)

        print("Parabens voce contratou o sevico")

    def CheckOffer(id_player):
        print("Ofertas ativas")
        offers = Database.DB.CheckActiveContracts(id_player)

        index = ["Identificador: ", "Usuario: ", "Localidade: ", "Preco: ", "Dias: "]
        for tup in offers:
            i = 0
            Utils.Util.Separator(False)
            for ele in tup:
                print(f"{index[i]}{ele}")
                i += 1

        Utils.Util.Separator(False)

        print("Digite o numero do identificador para deletar, ou 0 para sair")
        x = ""
        i = 0
        t = Database.DB.GetOfferID(id_player)
        while not(x in t):
            if i > 0:
                print("Escolha invalida, tente novamente")
            try:
                x = input("Escolha: ")
                if x == "0":
                    print("\n")
                    return
                x = int(x)
            except:
                print("Algo alem de numero foi escrito, tente novamente")

            i += 1

        Database.DB.DeleteActiveOffer(x)

        print("Deletado com sucesso")
    
    def ExportGraph(idp):
        
        t = Database.DB.GetSpent(idp)
        x = []
        y = []
        for tup in t:
            x.append(tup[0]) 
            y.append(tup[1]) 

        Utils.Util.Graph(x, y,"Meses", "Gasto", "Gastos mensais")

    def ExportReport(idp):
        
        t = Database.DB.GetSpent(idp)

        s = ""
        index = ["Mes: ", "Ganhos: "]
        for tup in t:
            x = 0
            s +=  Utils.Util.Separator(True)
            for i in tup:
                s += f"{index[x]}{i}\n"
                x += 1

        with open("relatorioCarona.txt", "w") as f:
            f.write(s)


if __name__ == "__main__":
    Carona.main()
