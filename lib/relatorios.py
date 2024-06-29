from app import livros, leitores


def produzirRelatorio():
    relatorio = []

    for livro in livros:
        if livro["disponivel"] == True:

            item = {
                "titulo": livro["titulo"],
                "disponivel": True,
                "multado": False,
            }
            relatorio.append(item)

        else:
            for leitor in leitores:
                if len(leitor["lista_multas"]) != 0:
                    for livro_indisponivel in leitor["lista_multas"]:
                        if livro_indisponivel["titulo"] == livro["titulo"]:
                            item = {
                                "titulo": livro["titulo"],
                                "disponivel": False,
                                "multado": True,
                                "leitor": leitor["nome"]
                            }
                            relatorio.append(item)
                        else:
                            item = {
                                "titulo": livro["titulo"],
                                "disponivel": False,
                                "multado": False,
                            }
                            relatorio.append(item)

    return relatorio


def imprimirRelatorio():
    relatorio = produzirRelatorio()

    lista = []

    for livro in relatorio:
        lista.append(livro["titulo"])

    maior_disponivel = len(max(lista, key=len))

    print("-"*(maior_disponivel+8))
    print("| ", end="")
    print("Disponiveis".center(maior_disponivel+4), end="")
    print(" |")

    indiceDisponiveis = 0
    for livro in relatorio:

        if livro["disponivel"] == True:
            indiceDisponiveis +=1
            print("| ", end="")
            print(f"{indiceDisponiveis} - ", end="")
            print(f"{livro["titulo"]}".ljust(maior_disponivel), end="")
            print(" |")

    print("-"*(maior_disponivel+8))
    print()
    

    print("-"*(maior_disponivel+8))
    print("| ", end="")
    print("Emprestados".center(maior_disponivel+4), end="")
    print(" |")

    indiceEmprestados = 0
    for livro in relatorio:

        if livro["disponivel"] == False:
            indiceEmprestados += 1
            print("| ", end="")
            print(f"{indiceEmprestados} - ", end="")
            print(f"{livro["titulo"]}".ljust(maior_disponivel), end="")
            print(" |")

    print("-"*(maior_disponivel+8))
    print()
    

    print("-"*(maior_disponivel+8))
    print("| ", end="")
    print("Multados".center(maior_disponivel+4), end="")
    print(" |")
    indiceMultados = 0
    for livro in relatorio:

        if livro["multado"] == True:
            indiceMultados += 1
            print("| ", end="")
            print(f"{indiceMultados} - ", end="")
            print(f"{livro["leitor"]}".ljust(maior_disponivel), end="")
            print(" |")
    print("-"*(maior_disponivel+8))
    print()
