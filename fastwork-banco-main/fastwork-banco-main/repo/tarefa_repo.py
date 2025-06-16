from sqlite3 import *
from sql.tarefa_sql import *
from data.database import obter_conexao
from models.tarefa import Tarefa


# Função para criar a tabela de tarefas
def criar_tabela_tarefa():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_TAREFA)
    conexao.commit()
    conexao.close()

# Função para listar tarefas em uma sessão de 20 tarefas (paginação)
def listar_tarefas_paginadas(offset):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(LISTAR_TAREFAS_PAGINADAS, (offset,))
    return cursor.fetchall()

# Função para inserir uma nova tarefa
def inserir_tarefa(descricao, empregador, endereco, valor, data, status) -> Tarefa:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        INSERIR_TAREFA,
        (descricao, empregador, endereco, valor, data, status),
    )
    conexao.commit()
    conexao.close()
    return Tarefa

# Função para editar uma tarefa para inserir valor e freelancer
def editar_tarefa_valor_freelancer(id_tarefa, valor, freelancer):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(
        EDITAR_TAREFA_VALOR_FREELANCER,
        (valor, freelancer, id_tarefa),
    )
    conexao.commit()
    conexao.close()

# Função para buscar uma tarefa pelo ID
def buscar_tarefa_por_id(id_tarefa):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(BUSCAR_TAREFA_POR_ID, (id_tarefa,))
    conexao.commit()
    conexao.close()
    return cursor.fetchone()

# Função para listar tarefas por empregador
def listar_tarefas_por_empregador(empregador_id):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(LISTAR_TAREFAS_POR_EMPREGADOR, (empregador_id,))
    return cursor.fetchall()

# Função para listar tarefas por freelancer
def listar_tarefas_por_freelancer(freelancer_id):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(LISTAR_TAREFAS_POR_FREELANCER, (freelancer_id,))
    return cursor.fetchall()