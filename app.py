
livros = [
    {"titulo": "O pequeno principe", "autor": "Antoine de Saint-Exupéry", "disponivel": True},
    {"titulo": "Homo Deus: Uma Breve História do Amanhã", "autor": "Yuval Harari", "disponivel": True},
    {"titulo": "Cálculo I", "autor": "James Stewart", "disponivel": False},
    {"titulo": "Geometria Analítica", "autor": "Reis e Silva", "disponivel": False},
]
leitores = [
    {"nome": "João Carlos da Silva", "livros": [], "multado": False, "lista_multas": []},
    {"nome": "Nascimento de Oliveira", "livros": [{"título": "Cálculo I", "data_devolucao": "03/07/2024"}], "multado": False, "lista_multas": []},
    {"nome": "Caio César", "livros": [{"título": "Geometria Analítica", "data_devolucao": "05/06/2024"}], "multado": True, "lista_multas": [{"título": "Geometria Analítica", "valor": 15}]},
]

def iniciar_aplicativo():
    opcao_escolhida = imprimirMenuPrincipalRetornaOpcao()
    while opcao_escolhida != 5:
        match opcao_escolhida:
            case 1:
                imprimirMenuLivros()
            case 2:
                print('Entrando em relatorios')
            case 3:
                print('Area do leitor')
            case 4:
                print('ajuda')
            case _:
                print('[!] Opção Inválida')
            
        
        opcao_escolhida = imprimirMenuPrincipalRetornaOpcao()


if __name__ == "__main__":
    from lib.menu import imprimirMenuPrincipalRetornaOpcao
    from lib.livros import imprimirMenuLivros
    iniciar_aplicativo()