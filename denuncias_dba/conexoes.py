# conexao.py
import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",          # troque se for outro usuário
            password="",
            database="sistema"
        )
        return conn
    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
        return None
