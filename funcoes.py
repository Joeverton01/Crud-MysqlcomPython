# funcoes.py
from conexoes import conectar


def cadastrar():
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    if not nome or not email:
        print("Nome e email são obrigatórios.")
        return

    con = conectar()
    if not con:
        return
    cursor = con.cursor()
    try:
        sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
        cursor.execute(sql, (nome, email))
        con.commit()
        print("Usuário cadastrado com sucesso! ID:", cursor.lastrowid)
    except Exception as e:
        print("Erro ao cadastrar:", e)
    finally:
        cursor.close()
        con.close()


def listar():
    con = conectar()
    if not con:
        return
    cursor = con.cursor()
    try:
        cursor.execute("SELECT id, nome, email FROM usuarios ORDER BY id")
        rows = cursor.fetchall()
        if not rows:
            print("Nenhum usuário encontrado.")
            return
        print("\n--- Usuários ---")
        for r in rows:
            print(f"{r[0]} - {r[1]} ({r[2]})")
    except Exception as e:
        print("Erro ao listar:", e)
    finally:
        cursor.close()
        con.close()


def atualizar():
    listar()
    id_usuario = input("Digite o ID do usuário que deseja atualizar: ").strip()
    if not id_usuario.isdigit():
        print("ID inválido.")
        return
    novo_nome = input("Novo nome (deixe vazio para manter): ").strip()
    novo_email = input("Novo email (deixe vazio para manter): ").strip()

    # Monta dinamicamente o UPDATE
    campos = []
    valores = []
    if novo_nome:
        campos.append("nome = %s")
        valores.append(novo_nome)
    if novo_email:
        campos.append("email = %s")
        valores.append(novo_email)
    if not campos:
        print("Nada a atualizar.")
        return

    valores.append(id_usuario)
    sql = f"UPDATE usuarios SET {', '.join(campos)} WHERE id = %s"

    con = conectar()
    if not con:
        return
    cursor = con.cursor()
    try:
        cursor.execute(sql, tuple(valores))
        con.commit()
        if cursor.rowcount:
            print("Atualizado com sucesso.")
        else:
            print("ID não encontrado.")
    except Exception as e:
        print("Erro ao atualizar:", e)
    finally:
        cursor.close()
        con.close()


def deletar():
    listar()
    id_usuario = input("Digite o ID do usuário que deseja deletar: ").strip()
    if not id_usuario.isdigit():
        print("ID inválido.")
        return
    confirm = input("Tem certeza? (s/N): ").lower()
    if confirm != "s":
        print("Operação cancelada.")
        return

    con = conectar()
    if not con:
        return
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        con.commit()
        if cursor.rowcount:
            print("Deletado com sucesso.")
        else:
            print("ID não encontrado.")
    except Exception as e:
        print("Erro ao deletar:", e)
    finally:
        cursor.close()
        con.close()
