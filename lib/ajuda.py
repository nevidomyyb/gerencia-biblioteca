def imprimirAjuda() -> None:
    texto = """
    ------------------------------------------------------------
           SISTEMA DE BIBLIOTECA - PÁGINA DE AJUDA
    ------------------------------------------------------------

    ÁREA DOS LIVROS
    1. Consultar Livro
    - Consultar todos
        - Use quando precisar ver todos os livros cadastrados no sistema.
    - Consultar por Título
        - Função usada para consultar livros com base no título.
    - Consultar por autor
        - Função usada para consultar livros com base no autor do livro.
    - Voltar

    2. Cadastrar livro
    - O usuário deve informar o título do livro e o autor.

    3. Emprestar Livro
    - Use quando precisar emprestar um livro, precisa de informações como: Nome do Leitor e Título do Livro
    - Voltar

    4. Relatórios
    - Visualize o relatório do sistema

    ÁREA DO LEITOR
    1. Cadastrar Leitor
    - Use para cadastrar um novo leitor no sistema
    2. Listar Leitores
    - Use para listar o nome dos leitores.
    3. Remover Leitor
    - Função usada para remover um leitor do sistema.
    4. Voltar

    SAIR
    - Utilize esta opção para sair do sistema.
    ------------------------------
    """
    print(texto)