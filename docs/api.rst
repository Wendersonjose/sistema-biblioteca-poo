Referência da API
=================

Esta seção documenta todas as classes, métodos e funções disponíveis no sistema.

.. automodule:: src.biblioteca_melhorada
   :members:
   :undoc-members:
   :show-inheritance:

Classe Livro
------------

.. autoclass:: src.biblioteca_melhorada.Livro
   :members:
   :inherited-members:
   :special-members: __init__, __str__

   A classe Livro representa um livro individual na biblioteca.

   **Atributos:**
   
   * ``titulo`` (str): Título do livro
   * ``autor`` (str): Autor do livro  
   * ``ano`` (int): Ano de publicação
   * ``isbn`` (str, opcional): Código ISBN
   * ``disponivel`` (bool): Se está disponível para empréstimo
   * ``data_emprestimo`` (datetime, opcional): Data do empréstimo

   **Exemplo de uso:**

   .. code-block:: python

       livro = Livro("1984", "George Orwell", 1949, "978-0-452-28423-4")
       print(livro.disponivel)  # True
       
       # Emprestar
       if livro.emprestar():
           print("Livro emprestado com sucesso!")
       
       # Devolver
       livro.devolver()

Classe Usuario
--------------

.. autoclass:: src.biblioteca_melhorada.Usuario
   :members:
   :inherited-members:
   :special-members: __init__, __str__

   A classe Usuario gerencia usuários da biblioteca e seus empréstimos.

   **Atributos:**
   
   * ``nome`` (str): Nome do usuário
   * ``email`` (str, opcional): Email do usuário
   * ``livros_emprestados`` (List[Livro]): Lista de livros emprestados
   * ``limite_livros`` (int): Limite máximo de livros (padrão: 3)

   **Exemplo de uso:**

   .. code-block:: python

       usuario = Usuario("Ana Silva", "ana@email.com")
       livro = Livro("Clean Code", "Robert Martin", 2008)
       
       # Emprestar livro
       if usuario.pegar_livro(livro):
           print("Empréstimo realizado!")
       
       # Ver livros emprestados
       usuario.listar_livros_emprestados()
       
       # Devolver livro
       usuario.devolver_livro(livro)

Classe Biblioteca
-----------------

.. autoclass:: src.biblioteca_melhorada.Biblioteca
   :members:
   :inherited-members:
   :special-members: __init__

   A classe principal que gerencia toda a biblioteca.

   **Atributos:**
   
   * ``nome`` (str): Nome da biblioteca
   * ``livros`` (List[Livro]): Lista de todos os livros
   * ``usuarios`` (List[Usuario]): Lista de usuários registrados

   **Exemplo de uso:**

   .. code-block:: python

       biblioteca = Biblioteca("Biblioteca Central")
       
       # Adicionar recursos
       biblioteca.adicionar_livro(livro)
       biblioteca.registrar_usuario(usuario)
       
       # Consultas
       biblioteca.listar_livros()
       resultados = biblioteca.buscar_livro("python")
       biblioteca.estatisticas()

Métodos Detalhados
------------------

Livro.emprestar()
~~~~~~~~~~~~~~~~~

.. automethod:: src.biblioteca_melhorada.Livro.emprestar

   Empresta o livro se estiver disponível.
   
   **Retorna:**
       bool: True se emprestado com sucesso, False se já estiver emprestado
   
   **Efeitos colaterais:**
       * Define ``disponivel`` como False
       * Define ``data_emprestimo`` como datetime.now()

Livro.devolver()
~~~~~~~~~~~~~~~~

.. automethod:: src.biblioteca_melhorada.Livro.devolver

   Devolve o livro, tornando-o disponível novamente.
   
   **Efeitos colaterais:**
       * Define ``disponivel`` como True
       * Remove ``data_emprestimo`` (None)

Usuario.pegar_livro()
~~~~~~~~~~~~~~~~~~~~~

.. automethod:: src.biblioteca_melhorada.Usuario.pegar_livro

   Tenta emprestar um livro para o usuário.
   
   **Parâmetros:**
       livro (Livro): O livro a ser emprestado
   
   **Retorna:**
       bool: True se emprestado com sucesso
   
   **Validações:**
       * Verifica se usuário não excedeu limite de livros
       * Verifica se livro está disponível
   
   **Exemplo:**
   
   .. code-block:: python
   
       usuario = Usuario("João")
       livro = Livro("1984", "Orwell", 1949)
       
       if usuario.pegar_livro(livro):
           print("✅ Empréstimo realizado")
       else:
           print("❌ Não foi possível emprestar")

Usuario.devolver_livro()
~~~~~~~~~~~~~~~~~~~~~~~~

.. automethod:: src.biblioteca_melhorada.Usuario.devolver_livro

   Devolve um livro emprestado pelo usuário.
   
   **Parâmetros:**
       livro (Livro): O livro a ser devolvido
   
   **Retorna:**
       bool: True se devolvido com sucesso
   
   **Validações:**
       * Verifica se usuário realmente possui o livro

Biblioteca.buscar_livro()
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automethod:: src.biblioteca_melhorada.Biblioteca.buscar_livro

   Busca livros por título ou autor (case-insensitive).
   
   **Parâmetros:**
       termo (str): Termo de busca
   
   **Retorna:**
       List[Livro]: Lista de livros encontrados
   
   **Exemplo:**
   
   .. code-block:: python
   
       # Busca case-insensitive
       resultados = biblioteca.buscar_livro("PYTHON")  # Encontra "Python Fluente"
       resultados = biblioteca.buscar_livro("machado") # Encontra livros do Machado
       
       for livro in resultados:
           print(f"Encontrado: {livro}")

Biblioteca.estatisticas()
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automethod:: src.biblioteca_melhorada.Biblioteca.estatisticas

   Exibe estatísticas detalhadas da biblioteca.
   
   **Estatísticas incluem:**
   
   * Total de livros no acervo
   * Livros disponíveis
   * Livros emprestados  
   * Usuários registrados
   * Taxa de utilização (%)
   
   **Exemplo de saída:**
   
   .. code-block:: text
   
       📊 ═══ Estatísticas da Biblioteca Central ═══
       📚 Total de livros: 15
       ✅ Livros disponíveis: 12
       📤 Livros emprestados: 3
       👥 Usuários registrados: 8
       📈 Taxa de utilização: 20.0%

Validações e Exceções
---------------------

O sistema implementa validações robustas que geram exceções apropriadas:

ValueError - Dados Inválidos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As seguintes situações geram ``ValueError``:

**Classe Livro:**

.. code-block:: python

    # Título vazio
    Livro("", "Autor", 2020)  # ValueError: Título não pode estar vazio
    
    # Autor vazio  
    Livro("Título", "", 2020)  # ValueError: Autor não pode estar vazio
    
    # Ano inválido
    Livro("Título", "Autor", -100)  # ValueError: Ano inválido para o livro
    Livro("Título", "Autor", 3000)  # ValueError: Ano inválido para o livro

**Classe Usuario:**

.. code-block:: python

    # Nome vazio
    Usuario("")  # ValueError: Nome não pode estar vazio

**Classe Biblioteca:**

.. code-block:: python

    # Nome vazio
    Biblioteca("")  # ValueError: Nome da biblioteca não pode estar vazio

Tratamento Recomendado
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    try:
        livro = Livro(titulo_input, autor_input, int(ano_input))
        biblioteca.adicionar_livro(livro)
        print("✅ Livro adicionado com sucesso!")
        
    except ValueError as e:
        print(f"❌ Erro de validação: {e}")
        
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

Type Hints
----------

Todas as funções incluem type hints completos para melhor IDE support:

.. code-block:: python

    from typing import List, Optional
    from datetime import datetime
    
    def pegar_livro(self, livro: Livro) -> bool:
        """Type hints claros para IDE support"""
        pass
    
    def buscar_livro(self, termo: str) -> List[Livro]:
        """Retorna lista tipada de livros"""
        pass

Isso permite:

* **Autocompletar** no IDE
* **Verificação de tipos** com mypy
* **Documentação automática**
* **Refatoração segura**