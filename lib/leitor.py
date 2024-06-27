from .utils.criar_menus import imprimirMenusRetornandoOpcao
from .utils.encontrar_unico_leitor import encontrarUnicoLeitor
from app import leitores


def removerLeitor():
    nome = input("Digite o nome do leitor a ser removido: ")
    procura = encontrarUnicoLeitor(nome)

    if procura == None:
        print("[!] Leitor não encontrado!")
    else:
        del leitores[procura]
        print("[!] Leitor removido com sucesso!\n")


def listarLeitores():
    leitoresEncontrados = []
    for leitor in leitores:
        leitoresEncontrados.append(leitor["nome"])

    if len(leitoresEncontrados) != 0:
        maior_nome = len(max(leitoresEncontrados, key=len))
        contador = 1
        print('-'*(maior_nome + 6))
        for nome in leitoresEncontrados:
            print(f"{contador}".ljust(2), end="")
            print("|".ljust(2), end="")
            print(f"{nome}".center(maior_nome), end="")
            print("|".rjust(2))
            contador += 1
        print('-'*(maior_nome + 6))
        print()
    else:
        print("[!] Nenhum leitor encontrado!\n")


def cadastrarLeitor():

    nome = input("Nome do leitor: ")
    leitores.append({"nome": nome, "livros": [],
                    "multado": False, "lista_multas": []})
    print("[!] Leitor cadastrado com sucesso\n")


def imprimirMenuLeitor():
    lista_string = ['[1] Cadastrar Leitor',
                    '[2] Listar Leitores', '[3] Remover Leitor', '[4] Voltar']

    opc = imprimirMenusRetornandoOpcao(lista_string, "Área do Leitor")

    while opc != 4:
        match opc:
            case 1:
                cadastrarLeitor()
            case 2:
                listarLeitores()
            case 3:
                removerLeitor()
            case 4:
                break
            case _:
                print("[!] Opção Inválida")
        opc = imprimirMenusRetornandoOpcao(lista_string, "Área do Leitor")
