from .utils.criar_menus import imprimirMenusRetornandoOpcao
from .utils.remover_acento import removerAcentos
from .utils.encontrar_unico_livro import encontrarUnicoLivro
from .utils.encontrar_unico_leitor import encontrarUnicoLeitor
from app import livros, leitores
from typing import List
import datetime

def imprimirListaDeLivros(lista: List) -> None:
    if len(lista) != 0:
        titulos = [livro["titulo"] for livro in lista]
        maior_livro = len(max(titulos, key=len))
        autores = [livro["autor"] for livro in lista]
        maior_autor = len(max(autores, key=len))
    else:
        maior_livro = 20
        maior_autor = 20
    print(f"Contador", end="")
    print(" | ",end="")
    print("Título".center(maior_livro), end="")
    print(" | ",end="")
    print("Autor".center(maior_autor), end="")
    print(" | ",end="")
    print("Status")
    if len(lista) != 0:
        for index, livro in enumerate(lista):
            print(f"{index+1}".ljust(8), end="")
            print(" | ",end="")
            print(f"{livro['titulo']}".ljust(maior_livro),end="")
            print(" | ",end="")
            print(livro["autor"].ljust(maior_autor), end="")
            print(" | ",end="")
            print("Disponível" if livro["disponivel"] == True else "Indisponível")
    else:
        print("Nenhum livro encontrado".center(63))
    
    
def consultarTodos() -> None:
    imprimirListaDeLivros(livros)
        
def consultarPorNome() -> None:
    print("[!]Separe cada título por , caso queira pesquisar múltiplos títulos")
    nomes = input("Título do livro a pesquisar: ").split(',')
    encontrados = []
    for nome in nomes:
        for livro in livros:
            if removerAcentos(nome.lower()).strip() in removerAcentos(livro["titulo"].lower()).strip():
                encontrados.append(livro)
    imprimirListaDeLivros(encontrados)
    
def consultarPorAutor() -> None:
    print("[!]Separe cada título por , caso queira pesquisar múltiplos títulos")
    autores = input("Autor para pesquisar: ").split(',')
    encontrados = []
    for autor in autores:
        for livro in livros:
            if removerAcentos(autor.lower()).strip() in removerAcentos(livro["autor"].lower()).strip():
                encontrados.append(livro)
    imprimirListaDeLivros(encontrados)    
    
def emprestarLivro() -> None:
    titulo = input("Título do livro a se emprestar: ")
    indice_livro = encontrarUnicoLivro(titulo)
    if indice_livro == None:
        print("[!] Livro não encontrado")
        return None
    if livros[indice_livro]["disponivel"] == False:
        print('[!] Livro não disponível')
        return None
    leitor = input("Nome do leitor a se emprestar: ")
    indice_leitor = encontrarUnicoLeitor(leitor)
    if indice_leitor == None:
        print("[!] Leitor não encontrado")
        return None
    if leitores[indice_leitor]["multado"] == True:
        print(f"[!] O leitor {leitores[indice_leitor]['nome']} possui multas pendentes e portanto não será possível fazer nenhum empréstimo")
        return None
    data_emprestimo = datetime.datetime.now()
    data_emprestimo_string = data_emprestimo.strftime("%d/%m/%Y")
    data_devolucao = data_emprestimo + datetime.timedelta(days=14)
    data_devolucao_string = data_devolucao.strftime("%d/%m/%Y")
    livros[indice_livro]["disponivel"] = False
    leitores[indice_leitor]['livros'].append({"titulo": livros[indice_livro]['titulo'], "data_devolucao": data_devolucao_string, "data_emprestimo": data_emprestimo_string})
    print("[!] Livro emprestado com sucesso")
    
    

def imprimirMenuConsultaLivro() -> None:
    lista_string = ['[1] Consultar todos', '[2] Consultar por título', '[3] Consulta por autor', '[4] Voltar']
    opc = imprimirMenusRetornandoOpcao(lista_string, "Consultar Livro")
    while opc != 4:
        match opc:
            case 1:
                consultarTodos()
            case 2:
                consultarPorNome()
            case 3:
                consultarPorAutor()
            case 4:
                break
            case _:
                print("[!] Opção Inválida")
        opc = imprimirMenusRetornandoOpcao(lista_string, "Consultar Livro")
    
def cadastrarLivro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    livros.append({"titulo": titulo, "autor": autor, "disponivel": True})
    print("[!] Livro cadastrado com sucesso")

def imprimirMenuLivros() -> None:
    lista_string = ['[1] Consultar Livro', '[2] Cadastrar Livro', '[3] Emprestar Livro', '[4] Voltar']
    opc = imprimirMenusRetornandoOpcao(lista_string, "Área dos Livros")
    while opc != 4:
        match opc:
            case 1:
                imprimirMenuConsultaLivro()
            case 2:
                cadastrarLivro()
            case 3:
                emprestarLivro()
            case 4:
                break
            case _:
                print("[!] Opção Inválida")
        opc = imprimirMenusRetornandoOpcao(lista_string, "Área dos Livros") 