import Database
import Motorista
import Carona
import Utils

def main():
    while True:
        x = PromptPrincipal()

        if x == 1:
            Login()
        else:
            Registro()

        Utils.Util.Clear()


def PromptPrincipal():
    while True:
        print("O que deseja fazer:")
        print("1- Login")
        print("2- Cadastrar-se")
        opcao = input("Escolha: ")

        if not(opcao.strip() in ["1", "2"]):
            print("Escolha invalida \nTeste novamente usando os numeros disponiveis")
        else:
            return int(opcao)

def Login():
    keyword = "CANCELAR"
    s = "Login cancelado\n\n"
    print(f"\nCaso queria cancelar a operacao, digite {keyword} em qualquer momento durante o login")

    user = input("Escreva seu usuario: ")
    
    if user == keyword:
        print(s)
        return -1

    pas = input("Escreva sua senha: ")
    
    if pas == keyword:
        print(s)
        return -1

    if Database.DB.Login(user, pas) != 1:
        print("Login desconhecido ou errado")
        return -1

    Utils.Util.Clear()

    if Database.DB.GetType(user) == 2:
        Motorista.Motorista.main(Database.DB.GetIDPlayer(user))
        exit(0)
    else:
        Carona.Carona.main(Database.DB.GetIDPlayer(user))
        exit(0)



def Registro():
    keyword = "CANCELAR"
    s = "Registro cancelado\n\n"
    print(f"\nCaso queria cancelar a operacao, digite {keyword} em qualquer momento durante o registro")
    pas, pasConf, t = "", "0", 0


    while pas != pasConf:
        if t > 0:
            print("\n\nSenha diferente, tente novamente\n\n")
        user = input("Escreva seu usuario: ")
    
        if user == keyword:
            print(s)
            return 

        pas = input("Escreva sua senha: ")
    
        if pas == keyword:
            print(s)
            return

        pasConf = input("Confirme sua senha: ")

        if pasConf == keyword:
            print(s)
            return 
        t += 1

   
    tipo = ""
    t = 0

    while not (tipo in ["1", "2"]):
        if t > 0:
            print("Escolha invalida, tente novamente")
        tipo = input("Voce quer ser motorista ou pedir carona: \n1- Pedir carona\n2- Ser motorista\nEscolha: ")
        t += 1

    user  = str(user.strip())
    pas = str(pas.strip())
    tipo = int(tipo)

    Database.DB.Register(user, pas, tipo)

    print("Cadastrado com sucesso\n\n")

    Utils.Util.Separator()





if __name__ == "__main__":
    main()
