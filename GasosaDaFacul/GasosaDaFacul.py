# import matplotlib as plt
import Database

def main():
    x = PromptPrincipal()
    if x == 1:
        while Login() < 0:
            PromptPrincipal()
    else:
        Registro()


def PromptPrincipal():
    while True:
        print("O que deseja fazer:")
        print("1- Login")
        print("2- Cadastrar-se")
        opcao = input("Escolha: ")

        if not(opcao in ["1", "2"]):
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

    # Checar no banco de dados o login
    return 0

def Registro():
    keyword = "CANCELAR"
    s = "Login cancelado\n\n"
    print(f"\nCaso queria cancelar a operacao, digite {keyword} em qualquer momento durante o login")

    pas = input("Escreva sua senha: ")
    
    if pas == keyword:
        print(s)
        return -1

    pasConf = input("Confirme sua senha: ")

    if pasConf == keyword:
        print(s)
        return -1

    if pas != pasConf:
        print("Login cancelado, senha diferente\n\n")
        return -1

    # salvar no banco de dados o register
    return 0



if __name__ == "__main__":
    main()




