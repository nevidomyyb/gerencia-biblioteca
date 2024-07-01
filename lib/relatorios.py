from app import livros, leitores
from datetime import date


def imprimirRelatorio():

    lista_disponiveis = []
    lista_emprestados = []
    lista_leitores_multados = []

    for livro in livros:
        if livro["disponivel"] == True:
            lista_disponiveis.append(livro["titulo"])
        else:
            for leitor in leitores:
                if len(leitor["lista_multas"]) != 0:
                    for livro_multado in leitor["lista_multas"]:
                        if livro["titulo"] == livro_multado["titulo"]:
                            entrada = f"{livro['titulo']} - {leitor['nome']}"
                            lista_emprestados.append(entrada)

                            lista_leitores_multados.append(leitor["nome"])
                else:
                    for livro_emprestado in leitor["livros"]:
                        if livro["titulo"] == livro_emprestado["titulo"]:
                            entrada = f"{livro['titulo']} - {leitor['nome']}"
                            lista_emprestados.append(entrada)

    lista_disponiveis.sort(key=len, reverse=True)
    lista_emprestados.sort(key=len, reverse=True)
    lista_leitores_multados.sort(key=len, reverse=True)

    if len(lista_disponiveis) != 0:
        maior_disponivel = len(max(lista_disponiveis, key=len))
        if maior_disponivel < 26:
            maior_disponivel = 26
    else:
        maior_disponivel = 26

    if len(lista_emprestados) != 0:
        maior_emprestado = len(max(lista_emprestados, key=len))
        if maior_emprestado < 34:
            maior_emprestado = 34
    else:
        maior_emprestado = 34

    if len(lista_leitores_multados) != 0:
        maior_multado = len(max(lista_leitores_multados, key=len))
        if maior_multado < 17:
            maior_multado = 17
    else:
        maior_multado = 17

    tamanho_maximo = max(len(lista_disponiveis), len(
        lista_emprestados), len(lista_leitores_multados))
    largura_maxima = (maior_disponivel + maior_emprestado + maior_multado + 12)

    data = date.today()
    data_string = f"Relatório dia {data.strftime('%d/%m/%Y')}"

    print(f"{data_string}")
    print('-'*largura_maxima)
    print("| ", end="")
    print("Livros Disponíveis".center(maior_disponivel), end="")
    print(" | ", end="")
    print("Livros Emprestados".center(maior_emprestado), end="")
    print(" | ", end="")
    print("Leitores Multados".center(maior_multado), end="")
    print(" |")

    for indice in range(tamanho_maximo):
        if indice < len(lista_disponiveis):
            print("| ", end="")
            print(lista_disponiveis[indice].ljust(maior_disponivel), end="")
            print(" | ", end="")
        else:
            print("| ", end="")
            print("".ljust(maior_disponivel), end="")
            print(" |", end=" ")

        if indice < len(lista_emprestados):
            print(lista_emprestados[indice].ljust(maior_emprestado), end="")
            print(" | ", end="")
        else:
            print("".ljust(maior_emprestado), end="")
            print(" | ", end="")

        if indice < len(lista_leitores_multados):
            print(lista_leitores_multados[indice].ljust(maior_multado), end="")
            print(" | ")
        else:
            print("".ljust(maior_multado), end="")
            print(" | ")

    print('-'*largura_maxima)
    print("| ", end="")
    print(f"Total: {len(lista_disponiveis)}".ljust(maior_disponivel), end="")
    print(" | ", end="")
    print(f"Total: {len(lista_emprestados)}".ljust(maior_emprestado), end="")
    print(" | ", end="")
    print(f"Total: {len(lista_leitores_multados)}".ljust(maior_multado), end="")
    print(" |")
    print()
    print()
