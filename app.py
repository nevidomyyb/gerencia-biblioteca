
livros = [
    {"titulo": "O pequeno principe", "autor": "Antoine de Saint-Exupéry", "disponivel": True},
    {"titulo": "Homo Deus: Uma Breve História do Amanhã", "autor": "Yuval Harari", "disponivel": True},
    {"titulo": "Cálculo I", "autor": "James Stewart", "disponivel": True}
]
leitores = []

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