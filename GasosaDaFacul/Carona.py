import Database


class Carona():
    def main(idp):
        id_player = idp
        e = ""
        while not(e in ["1", "2", "3", "4", "5"]):
            print("=-=" * 20)
            print("Menu principal")
            print("1 - Ver ofertas de carona")
            print("2 - Ver clientes")
            print("3 - Exportar relatorios")
            print("4 - Exportar graficos")
            print("5 - Sair")
            e = input("Escolha: ")
            
            if e == "1":
                print("Sucesso!")
            elif e == "2":
                print()
            elif e == "3":
                print()
            elif e == "4":
                print()

            e = ""

    def SeeOffers():
        print("\n")
        print("Ofertas")
        sql = """
            SELECT
            L.USUARIO,
            M.PRECO,
            M.LOCALIDADE,
            M.DIAS
            FROM gasosafacul.tbmotorista M
            JOIN gasosafacul.tblogin L ON L.ID = M.ID_PESSOA
        """





if __name__ == "__main__":
    Carona.main()
