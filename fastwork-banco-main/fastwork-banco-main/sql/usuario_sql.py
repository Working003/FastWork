# Comando para criar a tabela de usuários
CREATE_TABLE_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    habilidades TEXT
);
"""

# Comando para buscar um usuário pelo nome
BUSCAR_USUARIO_POR_NOME = """
SELECT * FROM usuario
WHERE nome = ?;
"""

# Comando para inserir um novo usuário
INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, telefone, data_nascimento, habilidades)
VALUES (?, ?, ?, ?, ?, ?);
"""

# Comando para listar usuários por habilidades
LISTAR_USUARIOS_POR_HABILIDADES = """
SELECT * FROM usuario
WHERE habilidades LIKE ?;
"""

# Comando para deletar um usuário pelo ID
DELETAR_USUARIO = """
DELETE FROM usuario
WHERE id = ?;
"""

# Comando para editar informações de um usuário
EDITAR_USUARIO = """
UPDATE usuario
SET nome = ?, email = ?, senha = ?, telefone = ?, data_nascimento = ?, habilidades = ?
WHERE id = ?;
"""

#listar ususarios por paginação
LISTAR_USUARIOS_POR_PAGINA = """
SELECT * FROM usuario
LIMIT ? OFFSET ?;
"""