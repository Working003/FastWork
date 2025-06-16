# Comando para criar a tabela de tarefas
CREATE_TABLE_TAREFA = """
CREATE TABLE IF NOT EXISTS tarefa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    empregador INTEGER NOT NULL,
    freelancer INTEGER,
    endereco TEXT NOT NULL,
    valor REAL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL,
    FOREIGN KEY (empregador) REFERENCES usuario (id),
    FOREIGN KEY (freelancer) REFERENCES usuario (id)
);
"""

# Comando para listar tarefas em uma sessão de 20 tarefas
LISTAR_TAREFAS_PAGINADAS = """
SELECT * FROM tarefa
LIMIT 20 OFFSET ?;
"""

# Comando para inserir uma nova tarefa
INSERIR_TAREFA = """
INSERT INTO tarefa (descricao, empregador, endereco, data, status)
VALUES (?, ?, ?, ?, ?, ?);
"""

# Comando para editar uma tarefa para inserir valor e freelancer
EDITAR_TAREFA_VALOR_FREELANCER = """
UPDATE tarefa
SET valor = ?, freelancer = ?
WHERE id = ?;
"""

# Comando para buscar uma tarefa pelo ID
BUSCAR_TAREFA_POR_ID = """
SELECT * FROM tarefa
WHERE id = ?;
"""

# Comando para listar tarefas por empregador
LISTAR_TAREFAS_POR_EMPREGADOR = """
SELECT * FROM tarefa
WHERE empregador = ?;
"""

# Comando para listar tarefas por freelancer
LISTAR_TAREFAS_POR_FREELANCER = """
SELECT * FROM tarefa
WHERE freelancer = ?;
"""