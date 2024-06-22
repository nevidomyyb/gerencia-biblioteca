from typing import List
from .limpar_terminal import limpar_terminal

def criarMenus(lista_string: List[str], titulo: str) -> None:
    maior_valor = len(max(lista_string, key=len))
    print('-'*maior_valor)
    print(titulo.center(maior_valor))
    print('-'*maior_valor)
    for string in lista_string:
        print(string)
    print('-'*maior_valor)

def imprimirMenusRetornandoOpcao(lista_string: List[str], titulo: str) -> int:
    while True:
        criarMenus(lista_string, titulo)
        try:
            opc = int(input(""))
            limpar_terminal()
            return opc
        except:
            continue