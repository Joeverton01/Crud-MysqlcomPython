from conexoes import conectar

TIPOS = {
    1: "Plásticos e Microplásticos",
    2: "Derramamento de Óleo",
    3: "Esgoto e Produtos químicos",
    4: "Lixo e Detritos",
    5: "Resíduos industriais",
    6: "Outros",
}

GRAVIDADES = {
    1: "Baixa",
    2: "Média",
    3: "Alta",
    4: "Crítica"
}


# ================================
#   FUNÇÃO SEGURA PARA INPUT NUMÉRICO
# ================================
def input_int(msg, minimo=None, maximo=None):
    while True:
        valor = input(msg)

        if not valor.isdigit():
            print("❌ Digite apenas números!")
            continue

        valor = int(valor)

        if minimo is not None and valor < minimo:
            print(f"❌ O valor deve ser no mínimo {minimo}.")
            continue

        if maximo is not None and valor > maximo:
            print(f"❌ O valor deve ser no máximo {maximo}.")
            continue

        return valor


# ================================
#        C A D A S T R A R
# ================================
def cadastrar_denuncia():
    con = conectar()
    if not con:
        return

    cursor = con.cursor()

    print("\n=== CADASTRAR DENÚNCIA ===")

    titulo = input("Título: ")
    localizacao = input("Localização: ")

    print("\nTipos de Denúncia:")
    for numero, nome in TIPOS.items():
        print(f"{numero} - {nome}")
    tipo_escolhido = input_int("Escolha o tipo (1 a 6): ", 1, 6)
    tipo = TIPOS[tipo_escolhido]

    print("\nGravidade:")
    for numero, nome in GRAVIDADES.items():
        print(f"{numero} - {nome}")
    gravidade_escolhida = input_int("Escolha a gravidade (1 a 4): ", 1, 4)
    gravidade = GRAVIDADES[gravidade_escolhida]

    descricao = input("Descrição: ")

    try:
        sql = """
            INSERT INTO denuncias (titulo, localizacao, tipo, gravidade, descricao)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (titulo, localizacao, tipo, gravidade, descricao))
        con.commit()
        print("\n✅ Denúncia cadastrada com sucesso!")

    except Exception as e:
        print("❌ Erro ao cadastrar:", e)


# ================================
#           L I S T A R
# ================================
def listar_denuncias():
    con = conectar()
    if not con:
        return

    cursor = con.cursor()
    try:
        cursor.execute("SELECT * FROM denuncias")
        resultados = cursor.fetchall()
    except Exception as e:
        print("❌ Erro ao listar denúncias:", e)
        return

    print("\n=== LISTA DE DENÚNCIAS ===")

    if not resultados:
        print("Nenhuma denúncia cadastrada.\n")
        return

    for denuncia in resultados:
        print(f"""
ID: {denuncia[0]}
Título: {denuncia[1]}
Localização: {denuncia[2]}
Tipo: {denuncia[3]}
Gravidade: {denuncia[4]}
Descrição: {denuncia[5]}
----------------------------
""")


# ================================
#        A T U A L I Z A R
# ================================
def atualizar_denuncia():
    con = conectar()
    if not con:
        return
    cursor = con.cursor()

    listar_denuncias()

    id_d = input_int("Digite o ID da denúncia que deseja atualizar: ", 1)

    print("Deixe em branco se não quiser alterar o campo.\n")

    novo_titulo = input("Novo título: ")
    nova_localizacao = input("Nova localização: ")

    print("\nTipos de Denúncia:")
    for n, nome in TIPOS.items():
        print(f"{n} - {nome}")
    novo_tipo = input("Novo tipo (1-6) ou deixe vazio: ")

    print("\nGravidade:")
    for n, nome in GRAVIDADES.items():
        print(f"{n} - {nome}")
    nova_gravidade = input("Nova gravidade (1-4) ou deixe vazio: ")

    nova_descricao = input("Nova descrição: ")

    campos = []
    valores = []

    if novo_titulo.strip():
        campos.append("titulo=%s")
        valores.append(novo_titulo)

    if nova_localizacao.strip():
        campos.append("localizacao=%s")
        valores.append(nova_localizacao)

    if novo_tipo.strip():
        if novo_tipo.isdigit() and 1 <= int(novo_tipo) <= 6:
            campos.append("tipo=%s")
            valores.append(TIPOS[int(novo_tipo)])
        else:
            print("❌ Tipo inválido. Mantendo o atual.")

    if nova_gravidade.strip():
        if nova_gravidade.isdigit() and 1 <= int(nova_gravidade) <= 4:
            campos.append("gravidade=%s")
            valores.append(GRAVIDADES[int(nova_gravidade)])
        else:
            print("❌ Gravidade inválida. Mantendo a atual.")

    if nova_descricao.strip():
        campos.append("descricao=%s")
        valores.append(nova_descricao)

    if not campos:
        print("⚠ Nada para atualizar.")
        return

    sql = f"UPDATE denuncias SET {', '.join(campos)} WHERE id_denuncia=%s"
    valores.append(id_d)

    try:
        cursor.execute(sql, valores)
        con.commit()
        print("\n✅ Denúncia atualizada com sucesso!")
    except Exception as e:
        print("❌ Erro ao atualizar:", e)


# ================================
#        D E L E T A R
# ================================
def deletar_denuncia():
    con = conectar()
    if not con:
        return
    cursor = con.cursor()

    listar_denuncias()

    id_d = input_int("Digite o ID da denúncia que deseja excluir: ", 1)

    try:
        cursor.execute("DELETE FROM denuncias WHERE id_denuncia=%s", (id_d,))
        con.commit()

        if cursor.rowcount > 0:
            print("\n🗑️ Denúncia removida com sucesso!")
        else:
            print("\n⚠ ID inexistente.")

    except Exception as e:
        print("❌ Erro ao deletar:", e)
