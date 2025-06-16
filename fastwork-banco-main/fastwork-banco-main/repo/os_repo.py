from sqlite3 import *
from sql.os_sql import *
from data.database import obter_conexao
from models.os import Ordemservico


# Função para criar a tabela de ordens de serviço (OS)
def criar_tabela_os():
    """Cria a tabela Usuario se ela não existir."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_OS)
    conexao.commit()
    conexao.close()

def obter_os_por_id (id : int) -> Ordemservico:
    """Obtém uma ordem de serviço pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(EXIBIR_OS_POR_ID, (id,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Ordemservico(
            id=resultado[0],
            empregador=resultado[1],
            avaliacao=resultado[2],
            freelancer=resultado[3],
            valor=resultado[4])
    return None

# Função para inserir uma nova ordem de serviço
def inserir_os(empregador, avaliacao, freelancer, valor) -> Ordemservico:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        INSERIR_OS,(empregador, avaliacao, freelancer, valor),)
    connect.commit()
    conexao.close()
    return Ordemservico

# Função para inserir ou atualizar a avaliação de uma ordem de serviço
def inserir_avaliacao(id, avaliacao):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        INSERIR_AVALIACAO,
        (avaliacao, id),
    )
    conexao.commit()
    conexao.close()
    return cursor.rowcount > 0

# Função para listar ordens de serviço por empregador com paginação
def listar_os_por_pagina_e(empregador,limite, offset):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        LISTAR_OS_POR_PAGINA_E,
        (empregador, limite, offset),
        )
    return cursor.fetchall()
        
# Função para listar ordens de serviço por freelancer com paginação
def listar_os_por_pagina_f(freelancer, limite, offset):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        LISTAR_OS_POR_PAGINA_F,
        (freelancer, limite, offset),)
    return cursor.fetchall()