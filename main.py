# main.py
from funcoes import cadastrar, listar, atualizar, deletar


def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            deletar()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
