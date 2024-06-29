
livros = [
    {"titulo": "O pequeno principe", "autor": "Antoine de Saint-Exupéry", "disponivel": True},
    {"titulo": "Homo Deus: Uma Breve História do Amanhã", "autor": "Yuval Harari", "disponivel": True},
    {"titulo": "Cálculo I", "autor": "James Stewart", "disponivel": False},
    {"titulo": "Geometria Analítica", "autor": "Reis e Silva", "disponivel": False},    
    {"titulo": "A cor que caiu do espaço", "autor": "H. P. Lovecraft", "disponivel": True},
    {"titulo": "O Chamado de Cthulhu", "autor": "H. P. Lovecraft", "disponivel": True},
]
leitores = [
    {"nome": "João Carlos da Silva", "livros": [], "multado": False, "lista_multas": []},
    {"nome": "Nascimento de Oliveira", "livros": [{"título": "Cálculo I", "data_devolucao": "09/07/2024", "data_emprestimo": "20/06/2024"}], "multado": False, "lista_multas": []},
    {"nome": "Caio César", "livros": [{"título": "Geometria Analítica", "data_devolucao": "04/06/2024", "data_emprestimo": "26/05/2024"}], "multado": True, "lista_multas": [{"titulo": "Geometria Analítica", "valor": 15}]},
]

def iniciar_aplicativo():
    opcao_escolhida = imprimirMenuPrincipalRetornaOpcao()
    while opcao_escolhida != 5:
        match opcao_escolhida:
            case 1:
                imprimirMenuLivros()
            case 2:
                imprimirRelatorio()
            case 3:
                imprimirMenuLeitor()
            case 4:
                imprimirAjuda()
            case _:
                print('[!] Opção Inválida.')
            
        
        opcao_escolhida = imprimirMenuPrincipalRetornaOpcao()


if __name__ == "__main__":
    from lib.menu import imprimirMenuPrincipalRetornaOpcao
    from lib.livros import imprimirMenuLivros
    from lib.relatorios import imprimirRelatorio
    from lib.leitor import imprimirMenuLeitor
    from lib.ajuda import imprimirAjuda
    iniciar_aplicativo()