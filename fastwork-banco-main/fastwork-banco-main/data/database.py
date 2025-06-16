import sqlite3


def obter_conexao():
    conexao = sqlite3.connect('dados.db')
    return conexao