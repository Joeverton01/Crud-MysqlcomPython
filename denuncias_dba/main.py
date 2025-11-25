from funcoes import (
    cadastrar_denuncia,
    listar_denuncias,
    atualizar_denuncia,
    deletar_denuncia
)


def menu():
    while True:
        print("""
==============================
      MENU DENÚNCIAS
==============================
1 - Cadastrar denúncia
2 - Listar denúncias
3 - Atualizar denúncia
4 - Deletar denúncia
0 - Sair
""")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_denuncia()
        elif opc == "2":
            listar_denuncias()
        elif opc == "3":
            atualizar_denuncia()
        elif opc == "4":
            deletar_denuncia()
        elif opc == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


menu()
