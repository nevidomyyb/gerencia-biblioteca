from app import livros, leitores
from datetime import date


def imprimirRelatorio():

    lista_disponiveis = []
    lista_emprestados = []
    lista_multados = []

    for livro in livros:
        if livro["disponivel"] == True:
            lista_disponiveis.append(livro["titulo"])
        else:
            for leitor in leitores:
                if len(leitor["lista_multas"]) != 0:
                    for livro_multado in leitor["lista_multas"]:
                        if livro["titulo"] == livro_multado["titulo"]:
                            lista_emprestados.append(livro["titulo"])
                            lista_multados.append(leitor["nome"])
                        else:
                            lista_emprestados.append(livro["titulo"])

    lista_disponiveis.sort(key=len, reverse=True)
    lista_emprestados.sort(key=len, reverse=True)
    lista_multados.sort(key=len, reverse=True)

    maior_disponivel = len(max(lista_disponiveis, key=len))
    maior_emprestado = len(max(lista_emprestados, key=len))
    maior_multado = len(max(lista_multados, key=len))

    tamanho_maximo = max(len(lista_disponiveis), len(
        lista_emprestados), len(lista_multados))
    largura_maxima = (maior_disponivel + maior_emprestado + maior_multado + 12)

    data = date.today()
    data_string = f"Relatório do dia {data.strftime('%d/%m/%Y')}"

    print(data_string.rjust(52))
    print('-'*largura_maxima)
    print(" | ", end="")
    print("Disponíveis".center(maior_disponivel), end="")
    print(" | ", end="")
    print("Emprestados".center(maior_emprestado), end="")
    print(" | ", end="")
    print("Multados".center(maior_multado), end="")
    print(" |")
    for indice in range(tamanho_maximo):
        if indice < len(lista_disponiveis):
            print(" | ", end="")
            print(lista_disponiveis[indice].ljust(maior_disponivel), end="")
            print(" | ", end="")
        else:
            print("".ljust(maior_disponivel), end="")
            print(" | ", end=" ")
        if indice < len(lista_emprestados):
            print(lista_emprestados[indice].ljust(maior_emprestado), end="")
            print(" | ", end="")
        else:
            print("".ljust(maior_emprestado), end="")
            print(" | ", end="")
        if indice < len(lista_multados):
            print(lista_multados[indice].ljust(maior_multado), end="")
            print(" | ")
        else:
            print("".ljust(maior_multado), end="")
            print(" | ")
    print('-'*largura_maxima)
    print(" | ", end="")
    print(f"Total: {len(lista_disponiveis)}".ljust(maior_disponivel), end="")
    print(" | ", end="")
    print(f"Total: {len(lista_emprestados)}".ljust(maior_emprestado), end="")
    print(" | ", end="")
    print(f"Total: {len(lista_multados)}".ljust(maior_multado), end="")
    print(" | ")
    print()
    print()
