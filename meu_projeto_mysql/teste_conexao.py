


import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # se estiver vazio no XAMPP
        database="sistema"
    )
    if con.is_connected():
        print("✅ Conectado com sucesso ao MySQL!")
except Exception as e:
    print("❌ Erro de conexão:", e)
finally:
    if con.is_connected():
        con.close()
