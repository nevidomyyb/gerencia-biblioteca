from .utils.criar_menus import imprimirMenusRetornandoOpcao

def imprimirMenuPrincipalRetornaOpcao() -> int:
    lista_string = ['[1] Área dos Livros', '[2] Relatórios', '[3] Área do Leitor', '[4] Ajuda', '[5] Sair']
    opc = imprimirMenusRetornandoOpcao(lista_string, "Menu Principal")
    return opc
