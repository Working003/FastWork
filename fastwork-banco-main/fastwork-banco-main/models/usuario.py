from dataclasses import dataclass

@dataclass

class Usuario:
    id: int
    nome: str
    email: str
    senha: str
    telefone: str
    data_nascimento: str
    habilidade: str