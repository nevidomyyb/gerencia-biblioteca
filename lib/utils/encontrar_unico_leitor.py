from app import leitores
from .remover_acento import removerAcentos

def encontrarUnicoLeitor(nome: str) -> int:
    for indice, leitor in enumerate(leitores):
        if removerAcentos(nome.lower()).strip() in removerAcentos(leitor["nome"].lower()).strip():
            return indice
    return None