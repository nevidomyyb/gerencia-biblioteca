from app import livros
from .remover_acento import removerAcentos

def encontrarUnicoLivro(titulo: str) -> int:
    for indice, livro in enumerate(livros):
        if removerAcentos(titulo.lower()).strip() in removerAcentos(livro["titulo"].lower()).strip():
            return indice
    return None