# Comando para criar a tabela de ordem de serviço (OS)
CREATE_TABLE_OS = """
CREATE TABLE IF NOT EXISTS ordem_servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empregador INTEGER NOT NULL,
    avaliacao REAL,
    freelancer INTEGER NOT NULL,
    valor REAL NOT NULL,
    FOREIGN KEY (empregador) REFERENCES usuario (id),
    FOREIGN KEY (freelancer) REFERENCES usuario (id)
);
"""

# Comando para exibir todas as ordens de serviço
EXIBIR_OS_POR_ID = """
SELECT * FROM ordem_servico
WHERE id = ?;
"""

# Comando para inserir uma nova ordem de serviço
INSERIR_OS = """
INSERT INTO ordem_servico (empregador, avaliacao, freelancer, valor)
VALUES (?, ?, ?, ?);
"""

# Comando para inserir ou atualizar a avaliação de uma ordem de serviço
INSERIR_AVALIACAO = """
UPDATE ordem_servico
SET avaliacao = ?
WHERE id = ?;
"""

# Comando para listar Os por paginação e empregador
LISTAR_OS_POR_PAGINA_E = """
SELECT * FROM ordem_servico
WHERE empregador = ?
LIMIT ? OFFSET ?;
"""

# Comando para listar os por paginação e freelancer
LISTAR_OS_POR_PAGINA_F = """
SELECT * FROM ordem_servico
WHERE freelancer = ?
LIMIT ? OFFSET ?;
"""